h_params_grid = {
    'Echo':{
        'StandardScaler': {
            'with_std': [True]
        },
        'Echo':{
            'K': [5, 25, 100],
            'min_examples_cluster': [10, 50, 100],
            'ensemble_size': [5, 25, 50],
            'W': [100, 500, 1000],
            'tau': [0.2, 0.6, 0.9],
            'verbose': [0],
            'random_state': [42],
            'init_algorithm': ['kmeans']
        }
    },
    "Minas": {
        "StandardScaler": {"with_std": [True]},
        "Minas": {
            "kini": [5, 25, 100],
            "cluster_algorithm": ["kmeans"],
            "window_size": [100, 500, 1000],
            "threshold_strategy": [1],
            "threshold_factor": [1.1],
            "min_short_mem_trigger": [10, 50, 100],
            "min_examples_cluster": [10, 50, 100],
            "update_summary": [False, True],
            "verbose": [0],
            "random_state": [42],
        },
    },
    "ECSMiner": {
        "StandardScaler": {"with_std": [True]},
        "ECSMiner": {
            "K": [5, 25, 100],
            "min_examples_cluster": [10, 50, 100],
            "ensemble_size": [5, 25, 50],
            "T_l": [100],
            "verbose": [0],
            "random_state": [42],
            "init_algorithm": ["kmeans"],
        },
    },
    "ECSMinerWF": {
        "StandardScaler": {"with_std": [True]},
        "ECSMinerWF": {
            "K": [5, 25, 100],
            "min_examples_cluster": [10, 50, 100],
            "ensemble_size": [5, 25, 50],
            "verbose": [0],
            "random_state": [42],
            "init_algorithm": ["kmeans"],
        },
    },
}

datasets = [
    {
        "target": "Room_Occupancy_Count",
        "filename": "room_occupancy_bin.csv",
    },
    {
        "target": "class",
        "filename": "rialto_bin.csv",
    },
    {
        "target": "class",
        "filename": "powersupply_bin.csv",
    },
    {
        "target": "Class",
        "filename": "gassensor_bin.csv",
    },
    {
        "target": "label",
        "filename": "nursery_bin.csv",
    },
    {"target": "Class", "filename": "connect4_bin.csv"},
    {"target": "class", "filename": "sensit_bin.csv"},
    {
        "target": "Class",
        "filename": "shuttle_bin.csv",
    },
    {"target": "class", "filename": "randomtree_mc.csv"},
    {"target": "class", "filename": "randomtree_bin.csv"},
    {"target": "class", "filename": "randomrbf_mc.csv"},
    {"target": "class", "filename": "randomrbf_bin.csv"},
    {"target": "class", "filename": "sensit.csv"},
    {"target": "Class", "filename": "connect4.csv"},
    {"target": "Class", "filename": "adult.csv"},
    {
        "target": "label",
        "filename": "nursery.csv",
    },
    {
        "target": "Class",
        "filename": "creditcard.csv",
    },
    {
        "target": "class",
        "filename": "elec.csv",
    },
    {
        "target": "Class",
        "filename": "gassensor.arff",
    },
    {
        "target": "class",
        "filename": "INSECTS-abrupt_balanced_norm.arff",
    },
    {
        "target": "class",
        "filename": "INSECTS-abrupt_imbalanced_norm.arff",
    },
    {
        "target": "class",
        "filename": "INSECTS-gradual_balanced_norm.arff",
    },
    {
        "target": "class",
        "filename": "INSECTS-gradual_imbalanced_norm.arff",
    },
    {
        "target": "class",
        "filename": "INSECTS-incremental-abrupt_balanced_norm.arff",
    },
    {
        "target": "class",
        "filename": "INSECTS-incremental-abrupt_imbalanced_norm.arff",
    },
    {
        "target": "class",
        "filename": "INSECTS-incremental_balanced_norm.arff",
    },
    {
        "target": "class",
        "filename": "INSECTS-incremental_imbalanced_norm.arff",
    },
    {
        "target": "class",
        "filename": "INSECTS-incremental-reoccurring_balanced_norm.arff",
    },
    {
        "target": "class",
        "filename": "INSECTS-incremental-reoccurring_imbalanced_norm.arff",
    },
    {
        "target": "class",
        "filename": "NOAA.arff",
    },
    {
        "target": "class",
        "filename": "powersupply.arff",
    },
    {
        "target": "class",
        "filename": "rialto.arff",
    },
    {
        "target": "Room_Occupancy_Count",
        "filename": "room_occupancy.csv",
    },
    {
        "target": "Class",
        "filename": "shuttle.csv",
    },
]

best_h_params = {
  "sensorstream_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 50,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 100,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.042632012939193546
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.03977228944323817
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.004168488051778962
    ]
  },
  "poker_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 500,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.02145862283121501
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.05568747742137776
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.024322365211122868
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "W": 500,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.003421628632035453
    ]
  },
  "PAMAP2_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 500,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.14277815451330017
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.21363205692010387
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 25,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.019245556734955798
    ]
  },
  "room_occupancy_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 50,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 100,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.4101475616399138
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.5729337324219934
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 50,
          "ensemble_size": 50,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.3907636976368921
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "W": 1000,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.08839153039815396
    ]
  },
  "rialto_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.0650826763433015
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.07780528191790771
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.023072374485529994
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 100,
          "ensemble_size": 50,
          "W": 100,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.1946761943854528
    ]
  },
  "powersupply_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 100,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.19325202829810353
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.059354347745750345
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.0353378715063176
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 5,
          "min_examples_cluster": 100,
          "ensemble_size": 25,
          "W": 100,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.33533391285701036
    ]
  },
  "gassensor_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.13172427417514385
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.2682069890905702
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.028109968648131117
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 50,
          "W": 100,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.027376912678653983
    ]
  },
  "nursery_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 100,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.01810099650464756
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.38492050164600167
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.03606739086093661
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "W": 100,
          "tau": 0.6,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.02455197980597542
    ]
  },
  "fars_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 500,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.08581580544220328
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.1919912903621537
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.07907278596475144
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "W": 100,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.014085969585760078
    ]
  },
  "connect4_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 50,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.015514260436347726
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.01815896034909233
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 100,
          "min_examples_cluster": 100,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.01448446386478518
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "W": 100,
          "tau": 0.6,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.014059525694680277
    ]
  },
  "sensit_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 100,
          "min_examples_cluster": 50,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.12565183396399854
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.13574031451418528
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.08511030973371865
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "W": 500,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.014132889337541168
    ]
  },
  "shuttle_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 100,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 500,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.28019699923176733
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.40192201591139287
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.10698273891345472
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "W": 100,
          "tau": 0.6,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.03903333139077205
    ]
  },
  "nds1_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 50,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 100,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.17540983864839085
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.5653204295241052
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.24375842949815774
    ]
  },
  "randomtree_mc.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.0753121434453999
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.09388821405348409
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.022014063154862287
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "W": 500,
          "tau": 0.6,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.019626164551593488
    ]
  },
  "randomtree_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.025477980171605165
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.04849098189499601
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 100,
          "min_examples_cluster": 100,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.021854551494713725
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "W": 100,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.015883744330450627
    ]
  },
  "randomrbf_mc.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 500,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.43698677114599976
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.6627028408242875
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.22920446497806485
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 100,
          "ensemble_size": 25,
          "W": 500,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.1043175445666296
    ]
  },
  "randomrbf_bin.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 50,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.36382553260037687
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.4563028720910639
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 25,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.11174040427065765
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "W": 500,
          "tau": 0.6,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.07115788112140932
    ]
  },
  "sensit.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 100,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 500,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.17702392938237294
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.17027336690204659
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.15798413112747034
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 100,
          "ensemble_size": 5,
          "W": 100,
          "tau": 0.6,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.020970604842550308
    ]
  },
  "connect4.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.015123165127076801
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.03250349380381862
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.012909626767844056
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "W": 100,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.04360472675208455
    ]
  },
  "fars.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 50,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.1540262567484824
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.14649049536116032
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.1532484934656061
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 25,
          "W": 1000,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.1674333794377614
    ]
  },
  "census.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.025472290092954625
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.061331191523072745
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 25,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.04766860745184382
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "W": 500,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.2731560001195899
    ]
  },
  "adult.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 100,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.04113229924991879
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.11100381205682902
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 50,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.04342492845145464
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 5,
          "min_examples_cluster": 100,
          "ensemble_size": 50,
          "W": 100,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.024405720006839087
    ]
  },
  "nursery.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 100,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.04006904799080859
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.2728111303503685
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.045419067692550795
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 5,
          "min_examples_cluster": 50,
          "ensemble_size": 25,
          "W": 1000,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.07722662654159775
    ]
  },
  "nds1.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 500,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.1426363442426369
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.3748006031429724
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 100,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.21661938127439892
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 5,
          "min_examples_cluster": 100,
          "ensemble_size": 5,
          "W": 500,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.4267590728587023
    ]
  },
  "creditcard.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 50,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.02477303357733455
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.04557172870919673
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.03594023837097144
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 100,
          "ensemble_size": 5,
          "W": 100,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.5079589962053314
    ]
  },
  "elec.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 500,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.03716425729437175
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.042694668634952096
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 50,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.028849996155990428
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "W": 100,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.013266373575094637
    ]
  },
  "gassensor.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 100,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 500,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.3588298019654802
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.3500336846973873
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.20404746913902688
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "W": 500,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.3498268870218809
    ]
  },
  "INSECTS-abrupt_balanced_norm.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.2087318388711053
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.19237218923019853
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.14846248940024934
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "W": 500,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.2340521963322749
    ]
  },
  "INSECTS-abrupt_imbalanced_norm.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 100,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.21416782394726994
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.2548629792995824
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.20334547724514707
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 25,
          "W": 1000,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.2712206136637812
    ]
  },
  "INSECTS-gradual_balanced_norm.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.144590310715689
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.1599955644864181
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.07095850340523652
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "W": 500,
          "tau": 0.6,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.21886667561314696
    ]
  },
  "INSECTS-gradual_imbalanced_norm.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.1593652236868491
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.18900472023019507
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.09798642032712128
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "W": 500,
          "tau": 0.6,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.21181054134916397
    ]
  },
  "INSECTS-incremental-abrupt_balanced_norm.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.18835155714698965
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.22245288157690896
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.18421389795192947
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "W": 500,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.2926185675921555
    ]
  },
  "INSECTS-incremental-abrupt_imbalanced_norm.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.19876468514676604
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.2522043505809863
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.20642309167327205
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 100,
          "ensemble_size": 25,
          "W": 500,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.26964460432615805
    ]
  },
  "INSECTS-incremental_balanced_norm.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 50,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.22417876380875243
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.184510092208178
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.11340539947136859
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 100,
          "ensemble_size": 25,
          "W": 500,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.24958415089488772
    ]
  },
  "INSECTS-incremental_imbalanced_norm.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.2140368122094061
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.2551138467547688
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.23881839367552068
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "W": 500,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.27172879907984465
    ]
  },
  "INSECTS-incremental-reoccurring_balanced_norm.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.13209845926078911
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.19073682721585003
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.09743569916048891
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 100,
          "ensemble_size": 25,
          "W": 500,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.19700444189235572
    ]
  },
  "INSECTS-incremental-reoccurring_imbalanced_norm.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 50,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.24985110735262603
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.2546111213377691
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.1996517466591571
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "W": 1000,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.26889428322915593
    ]
  },
  "INSECTS-out-of-control_norm.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 500,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.3500619762290221
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.34544069682437567
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.31793813381978175
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 100,
          "ensemble_size": 25,
          "W": 1000,
          "tau": 0.6,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.37843578064088096
    ]
  },
  "NOAA.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.0475388605064152
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.06707125502018048
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.024310363712938148
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "W": 100,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.01447677076872939
    ]
  },
  "powersupply.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 25,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 100,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.09391182960401911
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.162338366790812
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 5,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.19814472343493797
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 5,
          "min_examples_cluster": 50,
          "ensemble_size": 25,
          "W": 1000,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.19339581567884367
    ]
  },
  "rialto.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 500,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.15465104291660542
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.09368196822152162
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.04687522599884216
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 25,
          "W": 500,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.1289542701252938
    ]
  },
  "room_occupancy.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 100,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.5115307560499839
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.5015848203569525
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.1869856193402355
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 100,
          "ensemble_size": 50,
          "W": 100,
          "tau": 0.2,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.16771569614683138
    ]
  },
  "shuttle.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 5,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 50,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 100,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.4170399337150611
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.46563345363615216
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 100,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.3405400732779151
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 100,
          "ensemble_size": 5,
          "W": 1000,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.596269955377926
    ]
  },
  "sensorstream.arff": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.0784755992752337
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.05486215128596345
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.049223668733645184
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "W": 100,
          "tau": 0.9,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.07103683491997327
    ]
  },
  "poker.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": False,
          "verbose": 0
        }
      },
      0.06456533648296633
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 25,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.08843728308787974
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 25,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.03676751898070441
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 25,
          "min_examples_cluster": 100,
          "ensemble_size": 5,
          "W": 1000,
          "tau": 0.6,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.1306521303365309
    ]
  },
  "PAMAP2.csv": {
    "Minas": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Minas": {
          "kini": 100,
          "cluster_algorithm": "kmeans",
          "random_state": 42,
          "min_short_mem_trigger": 10,
          "min_examples_cluster": 10,
          "threshold_strategy": 1,
          "threshold_factor": 1.1,
          "window_size": 1000,
          "update_summary": True,
          "verbose": 0
        }
      },
      0.4440983611854778
    ],
    "ECSMiner": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMiner": {
          "K": 100,
          "min_examples_cluster": 10,
          "ensemble_size": 5,
          "T_l": 100,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.4807284719800138
    ],
    "ECSMinerWF": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "ECSMinerWF": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 5,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.2818243791415393
    ],
    "Echo": [
      {
        "StandardScaler": {
          "with_std": True
        },
        "Echo": {
          "K": 100,
          "min_examples_cluster": 50,
          "ensemble_size": 50,
          "W": 500,
          "tau": 0.6,
          "verbose": 0,
          "random_state": 42,
          "init_algorithm": "kmeans"
        }
      },
      0.44843722711983486
    ]
  }
}