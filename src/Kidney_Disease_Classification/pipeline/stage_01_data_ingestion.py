from src.Kidney_Disease_Classification.config.configuration import ConfigurationManager
from src.Kidney_Disease_Classification.components.data_ingestion import DataIngestion
from src.Kidney_Disease_Classification import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass



    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.data_ingestion_config()
        data_ingestion = DataIngestion(config= data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



if __name__ == "__main__":

    try:
        logger.info(f">>>>>>>>>>{STAGE_NAME} is started<<<<<<<<<<")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()

        logger.info(f">>>>>>>>>>{STAGE_NAME} is completed <<<<<<<<<<</n/n X====================X")

    except Exception as e:
        logger.info(e)
        raise e
