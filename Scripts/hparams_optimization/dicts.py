param_grid = {
    'Minas':{
        'StandardScaler': {
            'with_std': [True]
        },
        'Minas':{
            'kini': [5, 25, 100],
            'cluster_algorithm': ['kmeans'], 
            'window_size': [100, 500, 1000], 
            'threshold_strategy': [1], 
            'threshold_factor': [1.1], 
            'min_short_mem_trigger': [10, 50, 100], 
            'min_examples_cluster': [10, 50, 100],
            'update_summary': [False, True],
            'verbose': [0],
            'random_state': [42],
        }
    },
    'ECSMiner':{
        'StandardScaler': {
            'with_std': [True]
        },
        'ECSMiner':{
            'K': [5, 25, 100],
            'min_examples_cluster': [10, 50, 100],
            'ensemble_size': [5, 25, 50],
            'T_l': [100],
            'verbose': [0],
            'random_state': [42],
            'init_algorithm': ['kmeans']
        },
    },
    'ECSMinerWF':{
        'StandardScaler': {
            'with_std': [True]
        },
        'ECSMinerWF':{
            'K': [5, 25, 100],
            'min_examples_cluster': [10, 50, 100],
            'ensemble_size': [5, 25, 50],
            'verbose': [0],
            'random_state': [42],
            'init_algorithm': ['kmeans']
        },
    },
}

datasets = [
    {
        'target': 'class',
        'filename': 'elec.csv',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'luxembourg.csv',
        'known_class': 0
    },
    {
        'target': 'Class',
        'filename': 'ozone.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'sensorstream.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'poker.csv',
        'known_class': 0
    },
    {
        'target': 'Class',
        'filename': 'gassensor.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'powersupply.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'rialto.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'outdoor.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'keystroke.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'NOAA.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'INSECTS-abrupt_balanced_norm.arff',
        'known_class': 0
    },
    {
        'target': 'Class',
        'filename': 'shuttle.csv',
        'known_class': 1
    },
    {
        'target': 'Class',
        'filename': 'creditcard.csv',
        'known_class': 0
    },
    {
        'target': 'Room_Occupancy_Count',
        'filename': 'room_occupancy.csv',
        'known_class': 0
    },
    {
        'target': 'activityID',
        'filename': 'PAMAP2.csv',
        'known_class': 1
    },
]