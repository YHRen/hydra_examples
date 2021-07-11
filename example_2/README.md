# Hydra Initialization

Add the `__target__` in the config file to point to the python class the config is to control.

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

## Exercise 1: instantiate

In the `mlp.yaml`, add `_target_: example_2.network.MLP`. 

In the `main.py`, import instantiate method, 
`from hydra.utils import instantiate`  and call
`model = instantiate(cfg.model)

`python main.py `

## Exercise 2: Change OmegaConf List to python list

Notice that, by default, the passed in list is `omegaconf.listconfig.ListConfig`.

We can control it conversion behavior by `_convert_`: 
`model = instantiate(cfg.model, _convert_="partial")`

After change this line in `main.py`, run `python main.py`

## Exercise 3: Recursive Instantiation 

Take a look at `cnn.yaml`, and run 

`python main.py model=cnn`

Change the activation to `PReLU`. 

`python main.py model=cnn "model/act=prelu"`
