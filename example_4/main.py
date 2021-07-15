from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    if cfg.get("dry_run", False):
        print("~~~DRY RUN~~")
    else:
        print("~~~REAL RUN~~")

if __name__ == "__main__":
    print("hydra version: ", hydra.__version__)
    my_app()
