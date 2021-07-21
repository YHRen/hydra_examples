import logging
from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    cfg_dict = OmegaConf.to_yaml(cfg)
    logging.info(cfg_dict)

if __name__ == "__main__":
    #print("hydra version: ", hydra.__version__)
    my_app()
