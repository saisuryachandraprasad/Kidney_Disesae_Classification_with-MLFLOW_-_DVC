from src.Kidney_Disease_Classification.constants import *
from src.Kidney_Disease_Classification.utils.common import read_yaml, create_directory
from src.Kidney_Disease_Classification.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directory([self.config.artifacts_root])

    def data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directory([config.root_dir])


        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_path = config.local_data_path,
            unzip_data_path = config.unzip_data_path

        )
        return data_ingestion_config