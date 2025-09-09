from dataclasses import dataclass
from omegaconf import OmegaConf, DictConfig, MISSING
import hydra
from hydra.core.config_store import ConfigStore
from typing import Any

# @dataclass
# class Resnet18:
#     model: str = "resnet18"
#     nrof_epochs: int = 30
#     learning_rate: float = 5e-3

# @dataclass
# class MyConfig:
#     training: ExperimentConfig = ExperimentConfig()
#     loss: LossConfig = LossConfig()
#     Res: Resnet18 = Resnet18()

# Inheritence
@dataclass
class Experiment:
    model: str = MISSING
    nrof_epochs: int = 30
    learning_rate: float = 5e-3

@dataclass
class Resnet18(Experiment):
    model: str = "resnet18"
    batch_size: int = 256

@dataclass
class Resnet50(Experiment):
    model: str = "resnet50"
    lr_scheduler: str = "MultiStepLR"

@dataclass
class Config:
    experiment: Any

cs = ConfigStore.instance()
cs.store(name="config", node=Config)
cs.store(group="experiment", name="resnet18", node=Resnet18)
cs.store(group="experiment", name="resnet50", node=Resnet50)

@hydra.main(config_path=None, config_name="config", version_base=None)
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()
