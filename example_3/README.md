# Non-mutual-exclusive Setting

Often times in ML applications we'd like to include a list of metrics or callbacks. 
For example, we'd like to monitor the model performance in terms of MSE, MAE, F1, mAP and so on.
We can create a configuration group named `metrics` and put all different choices inside it.

```
.
├── conf
│   ├── config.yaml
│   ├── dataset
│   │   ├── cifar10.yaml
│   │   └── mnist.yaml
│   ├── metrics
│   │   ├── f1.yaml
│   │   ├── mae.yaml
│   │   └── mse.yaml
│   └── model
│       ├── act
│       │   ├── prelu.yaml
│       │   └── relu.yaml
│       ├── cnn.yaml
│       └── mlp.yaml
├── main.py
└── README.md
```

## Exercise 1: Include all metrics in the configuration. 

In the master configuration file `config.yaml`, we can list all the metrics we want to include 
under the `metrics` option. 

```
defaults:
  - model: mlp
  - dataset: mnist
  - metrics:
    - mae
    - mse
```

Try to add more configurations, and run `python main.py`.


## Exercise 2: change the metrics list in the command line


To remove mse and add f1 metric in the command line.

```
python main.py 'metrics=[mae,f1]'
```


## Reference

[Selecting multiple configs from a Config Group](https://hydra.cc/docs/patterns/select_multiple_configs_from_config_group)
