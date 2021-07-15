# Configure Experiments 

As your configuration expands, you will quickly find that changing all the
configurations you'd like to change will end up with mutliple lines of command.
In this session, let's take a look how to group the common changes into an exeriment.

Take a look at the `experiments` folder.

Add the `__target__` in the config file to point to the python class the config
is to control.

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

## Exercise 1: create a dry run experiment yaml

```
# @package _global_
defaults:
  - override /model: cnn
  - override /dataset: cifar10
  
dry_run: true
```

In the dry run, we have replaced the model and dataset and defined a new flag
`dry_run` so we can take special care in the `main.py`.

```python
    if cfg.get("dry_run", False):
        print("~~~DRY RUN~~")
    else:
        print("~~~REAL RUN~~")
```

```
python main.py +experiment=dry_run
```

## Exercise 2: create two metrics experiments

```
python main.py +experiment=f1_exp
```

```
python main.py +experiment=mse_exp
```

Or run them in a sweep fashion:

```
python main.py -m '+experiment=glob(*_exp)'
```


## Exercise 3: configure hydra output folder

Hydra has default output directory as `output` and default sweep directory `multiprun`.

It is very likely we want to organize different experiments in 
different folder.

Let's first take a look what knobs we can turn. Notice there is a  new
config file `./conf/hydra/config`.

```yaml
defaults:
  - job_logging : default     # Job's logging config
  - launcher: basic           # Launcher config
  - sweeper: basic            # Sweeper config
  - output: default           # Output directory
```

Let's run the following and take a look at the `hydra_default_options.txt`. 

```
python main.py --cfg hydra > hydra_default_options.txt
```

The defaut output folder rule is `dir: outputs/${now:%Y-%m-%d}/${now:%H-%M-%S}`  like so:
```
outputs
└── 2021-07-15
    └── 00-20-54
        ├── .hydra
        │   ├── config.yaml
        │   ├── hydra.yaml
        │   └── overrides.yaml
        └── main.log
```

This is quite waste of space if we do a lot of debugging dry runs. 
Let's change `hydra.run.dir` in `dry_run.yaml` to `/tmp` so we are not bothered.
We can stop outputing `.hydra` folder by assigning `hydra.output_subdir` to null.
Remind that `.hydra` contains all the config options we used to run the job.


## Exercise 4: Configure Hydra output folder part-II

A more useful way is to give different experiments 
a name and set the output accordingly.

Try to uncomment the lines in `f1_exp.yaml` and give it a try.


## Exercise 5: Adding a configuration group not in default list

(I haven't figured out how to do it in config file...)
But the command line works.


### Reference 

[Configuring Experiments](https://hydra.cc/docs/patterns/configuring_experiments)
[Configuring Hydra](https://hydra.cc/docs/configure_hydra/intro)
