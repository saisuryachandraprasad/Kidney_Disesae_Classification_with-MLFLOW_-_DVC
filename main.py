from src.Kidney_Disease_Classification.pipeline.stage_01_data_ingestion import DataIngestionPipeline
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