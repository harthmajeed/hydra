from omegaconf import DictConfig, OmegaConf
import hydra
from hydra.utils import get_original_cwd, to_absolute_path
import os
import logging

logger = logging.getLogger(__name__)

@hydra.main(config_path="configs_dir", config_name="config")
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config))
    print("CURRENT WORKING DIRECTORY: ", os.getcwd())
    print("ORIGINAL WORKING DIRECTORY: ", get_original_cwd())
    print("TO ABSOLUTE PATH('some_file.txt'): ", to_absolute_path("some_file.txt"))
    logger.info("some info message")
    logger.debug("some debug message")

if __name__ == "__main__":
    main()

#python .\main2.py -m tests=resnet18,resnet50 loss_func=arcface,cosface,softmax
#python .\main2.py -m tests='glob(*)' loss_func='glob(*, exclude=soft*)'

