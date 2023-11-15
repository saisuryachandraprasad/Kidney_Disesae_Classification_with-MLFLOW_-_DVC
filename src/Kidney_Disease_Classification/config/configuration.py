from src.Kidney_Disease_Classification.constants import *
from src.Kidney_Disease_Classification.utils.common import read_yaml, create_directory
from src.Kidney_Disease_Classification.entity.config_entity import (DataIngestionConfig,
                                                                    PrepareBaseModelConfig)


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
    


    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directory([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = config.root_dir,
            base_model_path = config.base_model_path,
            base_model_updated = config.base_model_updated,
            params_IMAGE_SIZE = self.params.IMAGE_SIZE,
            params_CLASSES = self.params.CLASSES,
            params_WEIGHTS = self.params.WEIGHTS,
            params_LEARNING_RATE = self.params.LEARNING_RATE,
            params_INCLUDE_TOP = self.params.INCLUDE_TOP

        )

        return prepare_base_model_config