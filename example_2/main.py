import logging
from omegaconf import DictConfig, OmegaConf
import hydra
from hydra.utils import instantiate 

@hydra.main(config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    logging.info(OmegaConf.to_yaml(cfg))
    model = instantiate(cfg.model)
    # model = instantiate(cfg.model, _convert_="partial")
    logging.info("instantiated model has type of "+repr(model))

if __name__ == "__main__":
    print("hydra version: ", hydra.__version__)
    my_app()
