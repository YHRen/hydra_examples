# Hydra Tutorials

## Getting Started

Key packages needed are `hydra` and `pytorch`.

```
conda env create -f requirements.yaml -n <your_env_name>
conda activate  <your_env_name>
```

If you are using pip and venv, 
```
python3 -m venv <your_env_name>
source <your_env_name>/bin/activate
pip install -r requirements.txt
```


## Motivation

There are several reasons why DL experiments are difficult to configure
-   Almost every aspects of DL contains hyperparameters. Different optimizers, datasets, neural network architecture related hyperparameters, different loss functions, and evaluation metrics.
-   Parameters for one class are not re-usable by other classes. For example, kernel-size in CNN cannot be used in MLP. This will make many command line arguments not useful.
-   Configuration file approach will easily lead to the configuration file explotion and hard to trace and make change.
-   DL research is very dynamic. For specific experiments, we may want to change a particular paramter.
-   The most common practice is to use configuration files along with CLI. Namely, to load a base configuration file and make some changes to finetune hyperparameters. (bash for loop)
-   Well... if one is really good at `sed`, probably change the config file on the fly in the bash script... 

Why now? Hydra1.1 added two very useful features.

## TOC

### example 1

Hydra basics: hierarchical config files and cli override.

Why useful? Best of both worlds: without writing parser to match config file.


### example 2

Instantiation and recursive instantiation

Why useful? Directly translate parsed dictionary to objects.

### example 3

Include more than one items in the same configuration group.

Why useful? For callbacks and metrics that we can add or delete.

### example 4

configure experiments and hydra output

Why useful? Better organization of experiments and their output.



TODO:
- [x] add list of metrics and how to configure in cli [link](https://hydra.cc/docs/patterns/select_multiple_configs_from_config_group)
- [x] configuring hydra
- [x] configure experiments [link](https://hydra.cc/docs/patterns/configuring_experiments)
- [ ] plugins: submitit (slurm), ray, optuna.
- [ ] integration with lightning.

