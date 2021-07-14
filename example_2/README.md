# Configurable object instantiation using Hydra

Add the `__target__` in the config file to point to the python class the config is to control.

```
.
├── conf
│   ├── config.yaml
│   ├── dataset
│   │   ├── cifar10.yaml
│   │   └── mnist.yaml
│   └── model
│       ├── act
│       │   ├── prelu.yaml
│       │   └── relu.yaml
│       ├── cnn.yaml
│       └── mlp.yaml
├── demo_pkg
│   └── network
│       ├── cnn.py
│       ├── __init__.py
│       └── mlp.py
├── main.py
└── README.md
```

## Exercise 1: instantiate

In the `mlp.yaml`, add `_target_: demo_pkg.network.MLP`. 

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

Take a look at `cnn.yaml`.
There are two ways to do recursive instantiation.

### in the defaults (recommended)

All the activations are grouped and placed in the folder `./conf/model/act/`.

To see the default ReLU activation:
`python main.py model=cnn`

Change the activation to `PReLU`:
`python main.py model=cnn "model/act=prelu"`

### inside the same config file

As the item `activation` `Sigmoid`. 
I have not found a way to change it in the command line.

