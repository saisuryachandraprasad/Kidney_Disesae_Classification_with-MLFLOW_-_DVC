from src.Kidney_Disease_Classification.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.Kidney_Disease_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.Kidney_Disease_Classification.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from src.Kidney_Disease_Classification.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
from src.Kidney_Disease_Classification import logger


STAGE_NAME = "Data Ingestion"
if __name__ == "__main__":

    try:
        logger.info(f">>>>>>>>>>{STAGE_NAME} is started<<<<<<<<<<")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()

        logger.info(f">>>>>>>>>>{STAGE_NAME} is completed <<<<<<<<<<</n/n X====================X")

    except Exception as e:
        logger.info(e)
        raise e
    


STAGE_NAME = "Prepare Base Model"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} is started<<<<<<<<<<<<<")

        prepare_base_mode_pipeline = PrepareBaseModelPipeline()
        prepare_base_mode_pipeline.main()

        logger.info(f">>>>>>>>>>>>>>> {STAGE_NAME} is completed <<<<<<<<<<<</n/nX==============X")

    except Exception as e:
        logger.info(e)
        raise e
    


STAGE_NAME = "Model Training"

if __name__ =="__main__":
    try:
        logger.info(f">>>>>>>>>>>>{STAGE_NAME} is started <<<<<<<<<<<<")

        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.main()

        logger.info(f">>>>>>>>>{STAGE_NAME} is completed<<<<<<<<<</n/n X=================X")

    except Exception as e:
        logger.info(e)
        raise e
    



STAGE_NAME = "Evaluation stage"

if __name__ == "__main__":
     
    try :
        logger.info("f>>>>>>>>>{STAGE_NAME} is started<<<<<<<<<<<<")

        model_evaliuation_pipeline = ModelEvaluationPipeline()
        model_evaliuation_pipeline.main()

        logger.info(f">>>>>>>>>>{STAGE_NAME} is completed /n/n X===========================X")

    except Exception as e:
        logger.info(e)
        raise e