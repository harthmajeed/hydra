from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(config_path="configs_dir", config_name="config")
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()

#python .\main2.py -m tests=resnet18,resnet50 loss_func=arcface,cosface,softmax
#python .\main2.py -m tests='glob(*)' loss_func='glob(*, exclude=soft*)'

