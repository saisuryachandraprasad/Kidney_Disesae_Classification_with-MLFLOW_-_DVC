import os
from src.Kidney_Disease_Classification.constants import *
from src.Kidney_Disease_Classification.utils.common import read_yaml, create_directory, save_json
from src.Kidney_Disease_Classification.entity.config_entity import (DataIngestionConfig,
                                                                    PrepareBaseModelConfig,
                                                                    ModelTrainerConfig,
                                                                    ModelEvaluationConfig)


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
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            base_model_updated = Path(config.base_model_updated),
            params_IMAGE_SIZE = self.params.IMAGE_SIZE,
            params_CLASSES = self.params.CLASSES,
            params_WEIGHTS = self.params.WEIGHTS,
            params_LEARNING_RATE = self.params.LEARNING_RATE,
            params_INCLUDE_TOP = self.params.INCLUDE_TOP

        )

        return prepare_base_model_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        training = self.config.training
        params = self.params
        prepare_base_model = self.config.prepare_base_model
        training_data = os.path.join(self.config.data_ingestion.unzip_data_path, "kidney-ct-scan-image")

        create_directory([Path(training.root_dir)])

        model_trainer_config = ModelTrainerConfig(
            root_dir = Path(training.root_dir),
            trained_model_path = Path(training.trained_model_path),
            base_model_updated = Path(prepare_base_model.base_model_updated),
            training_data = training_data,
            params_epochs = params.EPOCHS,
            params_batch_size = params.BATCH_SIZE,
            params_image_size = params.IMAGE_SIZE,
            params_augmentation = params.AUGMENTATION
        )
        return model_trainer_config
    
    
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        evaluation_config = ModelEvaluationConfig(
            path_of_model = "artifacts/training/model.h5",
            training_data = "artifacts/data_ingestion/kidney-ct-scan-image",
            all_params = self.params,
            mlflow_uri = "https://dagshub.com/saisuryachandraprasad/Kidney_Disesae_Classification_with-MLFLOW_-_DVC.mlflow",
            params_image_size = self.params.IMAGE_SIZE,
            params_batch_size = self.params.BATCH_SIZE
        )

        return evaluation_config