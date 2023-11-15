from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen= True)
class DataIngestionConfig:
    root_dir : Path
    source_url: str
    local_data_path: Path
    unzip_data_path: Path


@dataclass(frozen= True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    base_model_updated: Path
    params_IMAGE_SIZE: list
    params_CLASSES: int
    params_WEIGHTS: str
    params_LEARNING_RATE: float
    params_INCLUDE_TOP: bool