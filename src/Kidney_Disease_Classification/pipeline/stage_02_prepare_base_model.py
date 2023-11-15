from src.Kidney_Disease_Classification.config.configuration import ConfigurationManager
from src.Kidney_Disease_Classification.components.prepare_base_model import PrepareBaseModel
from src.Kidney_Disease_Classification import logger



STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass


    def main(self):
        config =  ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config= prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} is started<<<<<<<<<<<<<")

        prepare_base_mode_pipeline = PrepareBaseModelPipeline()
        prepare_base_mode_pipeline.main()

        logger.info(f">>>>>>>>>>>>>>> {STAGE_NAME} is completed <<<<<<<<<<<</n/nX==============X")

    except Exception as e:
        logger.info(e)
        raise e