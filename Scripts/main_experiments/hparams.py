h_params = {
    'elec.csv': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 500, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 5,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 5,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'luxembourg.csv': {
        'Minas':{
            'kini': 5,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 100, 
            'update_summary': False,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 5,
            'min_examples_cluster': 10,
            'ensemble_size': 5,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 5,
            'min_examples_cluster': 10,
            'ensemble_size': 5,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'ozone.arff': {
        'Minas':{
            'kini': 5,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 500, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 25,
            'min_examples_cluster': 10,
            'ensemble_size': 25,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 25,
            'min_examples_cluster': 100,
            'ensemble_size': 25,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'sensorstream.arff': {
        'Minas':{
            'kini': 25,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 100,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 25,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 5,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'poker.csv': {
        'Minas':{
            'kini': 5,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 50,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 25,
            'min_examples_cluster': 10,
            'ensemble_size': 5,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 5,
            'min_examples_cluster': 100,
            'ensemble_size': 5,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'gassensor.arff': {
        'Minas':{
            'kini': 25,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 100,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': False,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 25,
            'min_examples_cluster': 10,
            'ensemble_size': 25,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 5,
            'min_examples_cluster': 10,
            'ensemble_size': 25,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'powersupply.arff': {
        'Minas':{
            'kini': 5,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 5,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 5,
            'min_examples_cluster': 50,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'rialto.arff': {
        'Minas':{
            'kini': 25,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 500, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 5,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 5,
            'min_examples_cluster': 50,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'outdoor.arff': {
        'Minas':{
            'kini': 5,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 100, 
            'update_summary': False,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 5,
            'min_examples_cluster': 10,
            'ensemble_size': 5,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 5,
            'min_examples_cluster': 10,
            'ensemble_size': 5,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'keystroke.arff': {
        'Minas':{
            'kini': 25,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 50,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 100, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 25,
            'min_examples_cluster': 10,
            'ensemble_size': 5,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 25,
            'min_examples_cluster': 50,
            'ensemble_size': 5,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'NOAA.arff': {
        'Minas':{
            'kini': 5,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 100, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 25,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 25,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'INSECTS-abrupt_balanced_norm.arff': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'shuttle.csv': {
        'Minas':{
            'kini': 25,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 50,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 25,
            'min_examples_cluster': 10,
            'ensemble_size': 25,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 25,
            'min_examples_cluster': 50,
            'ensemble_size': 25,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'creditcard.csv': {
        'Minas':{
            'kini': 25,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 100,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 500, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 25,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 25,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'room_occupancy.csv': {
        'Minas':{
            'kini': 5,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 5,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 25,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'PAMAP2.csv': {
        'Minas':{
            'kini': 25,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 100,
            'min_examples_cluster': 10,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000,
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 25,
            'min_examples_cluster': 100,
            'ensemble_size': 25,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'INSECTS-abrupt_imbalanced_norm.arff': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'INSECTS-gradual_balanced_norm.arff ': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'INSECTS-gradual_imbalanced_norm.arff': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'INSECTS-incremental-abrupt_balanced_norm.arff': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'INSECTS-incremental-abrupt_imbalanced_norm.arff': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'INSECTS-incremental_balanced_norm.arff': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'INSECTS-incremental_imbalanced_norm.arff': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'INSECTS-incremental-reoccurring_balanced_norm.arff': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'INSECTS-incremental-reoccurring_imbalanced_norm.arff': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
    },
    'INSECTS-out-of-control_norm.arff': {
        'Minas':{
            'kini': 100,
            'cluster_algorithm': 'kmeans',
            'random_state': 42,
            'min_short_mem_trigger': 10,
            'min_examples_cluster': 50,
            'threshold_strategy': 1,
            'threshold_factor': 1.1,
            'window_size': 1000, 
            'update_summary': True,
            'verbose': 0,
        },
        'ECSMiner':{
            'K': 100,
            'min_examples_cluster': 10,
            'ensemble_size': 50,
            'T_l': 100,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
        },
        'ECSMinerWF':{
            'K': 100,
            'min_examples_cluster': 100,
            'ensemble_size': 50,
            'verbose': 0,
            'random_state': 42,
            'init_algorithm': 'kmeans'
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
    {
        'target': 'class',
        'filename': 'INSECTS-abrupt_imbalanced_norm.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'INSECTS-gradual_balanced_norm.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'INSECTS-gradual_imbalanced_norm.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'INSECTS-incremental-abrupt_balanced_norm.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'INSECTS-incremental-abrupt_imbalanced_norm.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'INSECTS-incremental_balanced_norm.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'INSECTS-incremental_imbalanced_norm.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'INSECTS-incremental-reoccurring_balanced_norm.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'INSECTS-incremental-reoccurring_imbalanced_norm.arff',
        'known_class': 0
    },
    {
        'target': 'class',
        'filename': 'INSECTS-out-of-control_norm.arff',
        'known_class': 0
    },
]