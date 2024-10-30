## Prioritizing the Essential: A Robust Evaluation Framework for Novelty Detection

This repository contains the code used in the empirical tests conducted in the paper *"Prioritizing the Essential: A Robust Evaluation Framework for Novelty Detection"* [1] as well as supplementary results.

This repository is organized as follows:
- **Figures** folder - contains all of the figures extracted from the experiments;
- **Notebooks** folder - contains the Jupyter Notebook used to extract and plot the figures, tables and results;
- **Scripts** folder - contains the necessary Python scripts to run the experiments on both synthetic and real datasets. Also shows the hyperparameters used in the experiments.
    - hparams_optimization/hparam_optim.py file - script containing the code to launch the hyperparameter optimization on all datasets using a grid search and save the results;
    - main_experiments/run_experiments.py file - script containing the code to launch the experiments on all datasets and collect the metric values;
    - dicts.py file - contains different data used by the scripts, including the hyperparameters used in the grid search, the information of all datasets, and the best hyperparameters found by the grid search;
    - helper_functions.py file - contains various helper functions used by the scripts to start the experiments, load/prepare the data, and others.
    

### Requirements
The experiments were implemented in Python. The code can be executed with the scripts located in the *Scripts* folder.

If you want to replicate the experiments by yourself, a working installation of Python (https://www.python.org/) is required as well as the following packages:

- Our package, StreamNDR (https://pypi.org/project/streamndr/)
- River (https://pypi.org/project/river/)
- Pandas (https://pypi.org/project/pandas/)
- Numpy (https://pypi.org/project/numpy/)
- Matplotlib (https://pypi.org/project/matplotlib/)
- Aim (https://pypi.org/project/aim/)
- Pathos (https://pypi.org/project/pathos/)
- Scikit-Learn (https://pypi.org/project/scikit-learn/)
- SciPy (https://pypi.org/project/scipy/)

### References
[1] *TBA*
