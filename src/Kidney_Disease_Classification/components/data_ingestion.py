import os
import zipfile
import gdown
from src.Kidney_Disease_Classification import logger
from src.Kidney_Disease_Classification.utils.common import get_size
from src.Kidney_Disease_Classification.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config


    def download_file(self) ->str:
        """Fetch data from url"""

        try:
            dataset_url = self.config.source_url
            zipdata_path = self.config.local_data_path

            os.makedirs("artifacts/data_ingestion", exist_ok=True)

            logger.info(f"Downloading is started")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='

            gdown.download(prefix+file_id, zipdata_path)

            logger.info("Downloaded data from url")
            
        except Exception as e:
            logger.info(e)
            raise e
        

    def extract_zip_file(self):
        """ This method is responsible for unziping the data"""

        unzip_dir = self.config.unzip_data_path
        os.makedirs(unzip_dir, exist_ok= True)

        with zipfile.ZipFile(self.config.local_data_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)

            
