from src.Kidney_Disease_Classification.config.configuration import ConfigurationManager
from src.Kidney_Disease_Classification.components.model_training import ModelTraining
from src.Kidney_Disease_Classification import logger


STAGE_NAME = "Model Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_training = ModelTraining(config= model_trainer_config)
        model_training.get_base_model()
        model_training.train_valid_generator()
        model_training.train()



if __name__ =="__main__":
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} is started <<<<<<<<<<<<")

        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.main()

        logger.info(f">>>>>>>>>{STAGE_NAME} is completed<<<<<<<<<</n/n X=================X")

    except Exception as e:
        logger.info(e)
        raise e