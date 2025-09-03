from omegaconf import OmegaConf, DictConfig
import hydra
import os

def main() -> None:
    #config = OmegaConf.load("./config.yaml")
    #my_items = ["training.batch_size=1024", "training.nrof_epochs=30", "training.optimizer.lr=5e-3"]
    #config = OmegaConf.from_dotlist(my_items)
    #config = OmegaConf.from_cli()
    
    config = OmegaConf.load("./config.yaml")
    config.training.scheduler = "MultiStepLR"
    print(OmegaConf.to_yaml(config))

    os.environ["USER"] = "majeedh"
    os.environ["PASSWORD1"] = "main_pass.py"

    config = OmegaConf.load("./var-interpolate-config.yaml")
    config = OmegaConf.load("./env-config.yaml")
    #print(OmegaConf.to_yaml(config, resolve=True))
    
    config_merge1 = OmegaConf.load("./merge-config1.yaml")
    config_merge2 = OmegaConf.load("./merge-config2.yaml")

    config = OmegaConf.merge(config_merge1, config_merge2)

    config.merge_with_cli()

    print(OmegaConf.to_yaml(config))

    #print("Learning Rate: ", config.training.lr)
    #print("Batch Size: ", config["training"]["batch_size"])

if __name__ == "__main__":
    main()
