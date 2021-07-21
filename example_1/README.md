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



## Exercise 0: Take a look at the content of all yaml files.

In `config.yaml` we can choose the default setting:

```
defaults:
  - model: cnn
  - dataset: mnist
```

* `defaults` is a keyword in hydra.
* key (e.g. dataset, model) needs to match the directory name
* value (e.g. cifar10, mlp) needs to match the file name.

## Exercise 1: Change CNN to MLP in CLI

`python main.py model=mlp dataset=cifar10`

## Exercise 2: Change MLP input dim to 64

`python main.py model=mlp model.mlp.input_dim=64`

## Exercise 3: Add additional argument on the fly 

`python main.py model=mlp +dry_run=true`

## Exercise 4: Multirun for different MLP hidden dims

Use `--multirun` or `-m` for short:
`python main.py -m model=mlp model.mlp.hidden_dims="[128, 64, 32],[64, 32, 16]"`

## Exercise 5: Note the changes of outputs and multirun folders

Note that, a default "outputs" and "multirun" folders are
created. All the hydra and config info are stored in
`.hydra`.  Very useful for reproducing the results and
debugging.

## Exercise 6: Install tab completion: bash, zsh, fish, etc

To see the instruction:
```
python main.py --hydra-help
```
