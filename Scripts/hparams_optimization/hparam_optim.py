import sys
import os
sys.path.append('/home/jgaud/projects/def-pbranco/jgaud/NoveltyDetectionMetricsExtension/streamndr-private')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from streamndr.metrics import ConfusionMatrixNovelty
from river.metrics import AdjustedMutualInfo
import time
import numpy as np
import math
import json
from streamndr.model import Minas, ECSMinerWF, ECSMiner, Echo

import math
import numpy as np
from tqdm import tqdm

from streamndr.metrics import ConfusionMatrixNovelty
from river.metrics import AdjustedMutualInfo
from river import preprocessing
from river import utils
import time
from itertools import repeat
import numpy as np
from pathos.pools import ProcessPool

import math

from dicts import h_params_grid, datasets
from helper_functions import *

def run_algo_mp(m, X_offline, y_offline, X_online, y_online, known_classes):
    try:
        m[0].learn_many(X_offline)
        m[1].learn_many(X_offline, y_offline)

        i = 0
        y_preds = []

        conf_matrix = ConfusionMatrixNovelty(known_classes)
        adj_mut_info = AdjustedMutualInfo(cm=conf_matrix)
        adj_mut_info_list = []

        for x, y_true in zip(X_online, y_online):
            start_time = time.time()
            x_dict = numpy2dict(x)
            m[0].learn_one(x_dict)
            x = m[0].transform_one(x_dict)
            
            if isinstance(x, dict):
                y_pred = m[1].predict_one(x, y_true) #predict_one takes python dictionaries as per River API
            else:
                y_pred = m[1].predict_many(x.reshape(1,-1), [y_true])
                

            if y_pred is not None: #Update our metrics
                y_preds.append(y_pred[0])

                conf_matrix.update(y_true, y_pred[0])
                
                if i % 100 == 0:
                    adj_mut_info_list.append(adj_mut_info.get())

            ## Print progress
            i += 1
            if i % 10000 == 0:
                print(i, '/', len(X_online), flush=True)

        return (m._get_params(), np.mean(adj_mut_info_list))
    
    except Exception as e:
        print(str(e), flush=True)
        return (m, -1)


def optimize_hp(algorithm, filename, target, n_jobs=4):
    baseline = {
        'ratio_wait_time_between_classes': 0,
        'sparsity': 1,
        'ratio_offline': 0.2,
        'ratio_known_classes': 0.2,
        'random_state': 42,
    }

    results = {}
    results[filename] = {}

    print(f'Dataset {filename}')
    
    if filename.endswith('.arff'):
        df = load_MOA(f'/home/jgaud/projects/def-pbranco/jgaud/NoveltyDetectionMetricsExtension/data/prepared_data/{filename}')
    elif filename.endswith('.csv'):
        df = load_CSV(f'/home/jgaud/projects/def-pbranco/jgaud/NoveltyDetectionMetricsExtension/data/prepared_data/{filename}')
    
    # Transform booleans to numeric values
    df = df.map(bool_to_int)

    n_samples = df.shape[0]
    sub_n_samples = min(max(math.floor(n_samples*0.05), 10000), n_samples)
    df = df.sample(n=sub_n_samples)

    
    known_classes = df[target].value_counts().index.tolist()[:math.ceil(baseline['ratio_known_classes']*len(np.unique(df[target])))]
    offline_df, online_df = prepare_data(df=df,
                                            param=baseline,
                                            ratio_wait_time_between_classes=baseline['ratio_wait_time_between_classes'], 
                                            sparsity=baseline['sparsity'], 
                                            ratio_offline=baseline['ratio_offline'],
                                            known_classes=known_classes,
                                            target=target, 
                                            random_state=baseline['random_state'],
                                            verbose=1)

    X_offline = offline_df.drop(target, axis=1)
    X_online = online_df.drop(target, axis=1).values
    y_offline = offline_df[target]
    y_online = online_df[target]
    
    if algorithm == 'Echo':
        model = (preprocessing.StandardScaler() | Echo())
    elif algorithm == 'Minas':
        model = (preprocessing.StandardScaler() | Minas())
    elif algorithm == 'ECSMiner':
        model = (preprocessing.StandardScaler() | ECSMiner())
    elif algorithm == 'ECSMinerWF':
        model = (preprocessing.StandardScaler() | ECSMinerWF())

    models = utils.expand_param_grid(model, h_params_grid[algorithm])

    scaler = preprocessing.StandardScaler()
    scaler.learn_many(X_offline)
    X_offline = scaler.transform_many(X_offline)

    pool = ProcessPool(n_jobs) #if 'large_file' not in ds else ProcessPool(5)

    pool.restart()

    avg_AMIs = []
    with tqdm(total=len(models)) as pbar:
        for result in pool.imap(run_algo_mp, models, repeat(X_offline), repeat(y_offline), repeat(X_online), repeat(y_online), repeat(known_classes)):
            # Update the progress bar
            pbar.update(1)
            print(result, flush=True)
            avg_AMIs.append(result)

    pool.close()
    pool.join()

    results[filename][algorithm] = max(avg_AMIs, key=lambda x: x[1])
    
    return results
    

if __name__ == '__main__':
    n_jobs = int(sys.argv[1])
    index = int(sys.argv[2])

    print(f'JOB #: {index}', flush=True)

    if index < 138:
        ds = index // 3
        alg = index % 3

        if alg == 0:
            best_model = optimize_hp('Minas', datasets[ds]['filename'], datasets[ds]['target'], n_jobs)
        elif alg == 1:
            best_model = optimize_hp('ECSMiner', datasets[ds]['filename'], datasets[ds]['target'], n_jobs)
        elif alg == 2:
            best_model = optimize_hp('ECSMinerWF', datasets[ds]['filename'], datasets[ds]['target'], n_jobs)
    
    else:
        ds = index - 138
        best_model = optimize_hp('Echo', datasets[ds]['filename'], datasets[ds]['target'], n_jobs)

    print(f'BEST MODEL: {best_model}', flush=True)

    with open(f'{index}_best_h_params', 'w') as file:
        json.dump(best_model, file)
