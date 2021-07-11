from omegaconf import DictConfig, OmegaConf
import hydra
from hydra.utils import instantiate 
import example_2
import torch

@hydra.main(config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    print(type(cfg.model), cfg.model)
    model = instantiate(cfg.model)
    # model = instantiate(cfg.model, _convert_="partial")
    print(type(model))

if __name__ == "__main__":
    print("hydra version: ", hydra.__version__)
    my_app()
