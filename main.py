from omegaconf import OmegaConf, DictConfig
import hydra

@hydra.main(config_path=None)
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()
