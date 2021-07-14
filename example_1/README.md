# Composable Configurations

```
conf
├── config.yaml
├── dataset
│   ├── cifar10.yaml
│   └── mnist.yaml
└── model
    ├── cnn.yaml
    └── mlp.yaml
```

In `config.yaml` we can choose the default setting:

```
defaults:
  - model: cnn
  - dataset: mnist
```

## Exercise 1: Change CNN to MLP

`python main.py model=mlp`

## Exercise 2: Change MLP input dim to 64

`python main.py model=mlp model.mlp.input_dim=64`

## Exercise 3: Add additional argument on the fly 

`python main.py model=mlp +dry_run=true`

## Exercise 4: Multirun for different MLP hidden dims

Use `--multirun` or `-m` for short:
`python main.py -m model=mlp model.mlp.hidden_dims="[128, 64, 32],[64, 32, 16]"`

## Logging

Note that, a default "outputs" and "multirun" folders are created. All the hydra and config info are stored. Very useful for reproducing the results and debugging.
