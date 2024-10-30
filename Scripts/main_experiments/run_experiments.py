import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('/home/jgaud/projects/def-pbranco/jgaud/NoveltyDetectionMetricsExtension/streamndr-private')
from streamndr.model import Minas, ECSMinerWF, ECSMiner, Echo

import math
import numpy as np
from aim import Run, Distribution

from streamndr.metrics import ConfusionMatrixNovelty, MNew, FNew, ErrRate, CER, TTD, TTC
from river.metrics import MacroF1, Rand, AdjustedRand, MutualInfo, AdjustedMutualInfo, VBeta, FowlkesMallows
from river import preprocessing
import time
import numpy as np

import math
from itertools import repeat
from tqdm import tqdm
from pathos.pools import ProcessPool

from dicts import best_h_params, datasets
from helper_functions import *

def online_training(clf, X_test, y_test, known_classes, scaler, aim_run=None, per_class_metrics=True, log_every=1):
    i = 0
    y_preds = []

    conf_matrix = ConfusionMatrixNovelty(known_classes)
    cer = CER(known_classes, cm=conf_matrix)
    m_new = MNew(known_classes, cm=conf_matrix)
    f_new = FNew(known_classes, cm=conf_matrix)
    err_rate = ErrRate(known_classes, cm=conf_matrix)
    ttd = TTD(known_classes)
    ttc = TTC(known_classes)
    rand_index = Rand(cm=conf_matrix)
    adj_rand_index = AdjustedRand(cm=conf_matrix)
    adj_mut_info = AdjustedMutualInfo(cm=conf_matrix)
    mut_info = MutualInfo(cm=conf_matrix)
    v_measure = VBeta(cm=conf_matrix)
    fowlkes_mallows = FowlkesMallows(cm=conf_matrix)
    

    for x, y_true in zip(X_test, y_test):
        start_time = time.time()

        x_dict = numpy2dict(x)
        scaler.learn_one(x_dict)
        x = scaler.transform_one(x_dict)
        
        if isinstance(x, dict):
            y_pred = clf.predict_one(x, y_true) #predict_one takes python dictionaries as per River API
        else:
            y_pred = clf.predict_many(x.reshape(1,-1), [y_true])
            

        if y_pred is not None: #Update our metrics
            y_preds.append(y_pred[0])

            conf_matrix.update(y_true, y_pred[0])
            ttd.update(y_true, y_pred[0])
            ttc.update(y_true, y_pred[0])
            
            if i % log_every == 0:

                try:
                    inv_harm_mean = 2 / ((1/(1-m_new.get())) + (1/(1-f_new.get())))
                except:
                    inv_harm_mean = 0.0

                try:
                    precision = conf_matrix.true_positives_novelty()/(conf_matrix.true_positives_novelty()+conf_matrix.false_positives_novelty())
                except:
                    precision = 0.0

                try:
                    recall = conf_matrix.true_positives_novelty()/(conf_matrix.true_positives_novelty()+conf_matrix.false_negatives_novelty())
                except:
                    recall = 0.0
    
                try:
                    f1s_binary = 2 * (precision * recall) / (precision + recall)
                except:
                    f1s_binary = 0.0

                try:
                    macro_f1 = MacroF1(cm=conf_matrix.get_associated_classes()).get()
                except:
                    macro_f1 = 0.0

                ##Update all metrics to Aim
                if aim_run is not None:
                    metrics_dict = {
                        'time_taken': time.time() - start_time,
                        'inv_m_new': 1-m_new.get(),
                        'inv_f_new': 1-f_new.get(),
                        'inv_harm_mean': inv_harm_mean,
                        'f1_binary': f1s_binary,
                        'macro_f1': macro_f1,
                        'unk_rate': clf.get_unknown_rate(),
                        'err_rate': err_rate.get(),
                        'cer': cer.get(),
                        'aic': cer.get_aic(),
                        'rand_index': rand_index.get(),
                        'adj_rand_index': adj_rand_index.get(),
                        'adj_mut_info': adj_mut_info.get(),
                        'mut_info': mut_info.get(),
                        'v_measure': v_measure.get(),
                        'fowlkes_mallows': fowlkes_mallows.get(),
                    }


                    aim_run.track(metrics_dict, step=i)

                    if per_class_metrics:
                        tmp = clf.get_class_unknown_rate()
                        for key in tmp:
                            aim_run.track(tmp[key], name='class_unk_rate_'+str(key), step=i, context={'metric': 'class_unk_rate', 'class': int(key)})

                        tmp = ttc.get()
                        for key in tmp:
                            aim_run.track(tmp[key], name='ttc_'+str(key), step=i, context={'metric': 'ttc', 'class': int(key)})

        ## Print progress
        i += 1
        if i % 5000 == 0:
                print(i, '/', len(X_test), flush=True)
    
    ## Update metrics on the last step
    if aim_run is not None:
        
        tmp = ttd.get()
        for key in tmp:
            aim_run.track(tmp[key], name='ttd_'+str(key), step=i-1, context={'metric': 'ttd', 'class': int(key)})
            
        d = Distribution(y_preds)
        aim_run.track(d, name='dist', step=i-1, context={'subset': 'y_preds'})
        
    
    return y_preds

def start_experiment(algorithm, param, target, df, h_params, n_samples, filename, aim_dir):
    try:
        start_time = time.time()
        
        print(f'Starting experiment with: {param}', flush=True)
        
        param['known_classes'] = df[target].value_counts().index.tolist()[:math.ceil(param['ratio_known_classes']*len(np.unique(df[target])))]
        offline_df, online_df = prepare_data(df=df,
                                                param=param,
                                                ratio_wait_time_between_classes=param['ratio_wait_time_between_classes'], 
                                                sparsity=param['sparsity'], 
                                                ratio_offline=param['ratio_offline'],
                                                known_classes=param['known_classes'],
                                                target=target, 
                                                random_state=param['random_state'],
                                                verbose=1)
    
        X_offline = offline_df.drop(target, axis=1)
        X_online = online_df.drop(target, axis=1).values
        y_offline = offline_df[target]
        y_online = online_df[target]
        
        run = setup_experiment(filename, algorithm, param, aim_dir)
        run['hparams'] = h_params


        if algorithm == 'Minas':
            clf = Minas(**h_params)
        elif algorithm == 'ECSMiner':
            clf = ECSMiner(**h_params)
        elif algorithm == 'ECSMinerWF':
            clf = ECSMinerWF(**h_params)
        elif algorithm == 'Echo':
            clf = Echo(**h_params)
        
        print('Computing offline phase...', flush=True)
        scaler = preprocessing.StandardScaler()
        scaler.learn_many(X_offline)
        X_offline = scaler.transform_many(X_offline)
        
        clf.learn_many(X_offline, y_offline)
        
        print('Computing online phase...', flush=True)
        online_training(clf, X_online, y_online, param['known_classes'], scaler, aim_run=run, per_class_metrics=True, log_every=100)
        
        run.finalize()
        
        print("--- %s seconds ---" % (time.time() - start_time), flush=True)

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    param_grid = {
        'ratio_wait_time_between_classes': [0, 0.1, 0.2],
        'sparsity': [0.1, 1, 100, 1000],
        'ratio_offline': [0.2, 0.5, 0.8],
        'ratio_known_classes': [0.2, 0.5, 0.6],
        'random_state': [42],
    }

    baseline = {
        'ratio_wait_time_between_classes': 0,
        'sparsity': 1,
        'ratio_offline': 0.2,
        'ratio_known_classes': 0.2
    }


    cpus = int(sys.argv[1])
    index = int(sys.argv[2])
    aim_dir = sys.argv[3]

    print(f'JOB #: {index}', flush=True)

    if index < 138:
        ds = index // 3
        alg = index % 3

    else:
        ds = index - 138
        alg = 3

    filename = datasets[ds]['filename']
    target = datasets[ds]['target']

    algorithm = {0: 'Minas', 1: 'ECSMiner', 2: 'ECSMinerWF', 3: 'Echo'}

    mc_parameters = generate_combinations(param_grid, baseline)
    param_grid['ratio_known_classes'] = [0.2]
    binary_parameters = generate_combinations(param_grid, baseline)

    print(f'Loading dataset {filename}...', flush=True)
    if filename.endswith('.arff'):
        df = load_MOA(f'/home/jgaud/projects/def-pbranco/jgaud/NoveltyDetectionMetricsExtension/data/prepared_data/{filename}')
    elif filename.endswith('.csv'):
        df = load_CSV(f'/home/jgaud/projects/def-pbranco/jgaud/NoveltyDetectionMetricsExtension/data/prepared_data/{filename}')
    else:
        print('File extension not supported', flush=True)

    # Transform booleans to numeric values
    df = df.map(bool_to_int)

    n_samples = df.shape[0]

    pool = ProcessPool(cpus)
    pool.restart()

    parameters = binary_parameters if len(np.unique(df[target])) == 2 else mc_parameters

    with tqdm(total=len(parameters)) as pbar:
        for result in pool.imap(start_experiment, repeat(algorithm[alg]), parameters, repeat(target), repeat(df), repeat(best_h_params[filename][algorithm[alg]][0][algorithm[alg]]), repeat(n_samples), repeat(filename), repeat(aim_dir)):
            # Update the progress bar
            pbar.update(1)

    pool.close()
    pool.join()