from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    base_model_path: Path
    params_image_size: list
    params_classes: int
    
@dataclass(frozen=True)
class PrepareWeightsConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path