import os
import urllib.request as request
import zipfile
from text_summarizer.logging import logger
from text_summarizer.utils.common import get_size
from pathlib import Path
from text_summarizer.entity import DataIngestionConfig
from text_summarizer.utils.common  import create_directories

import pdb


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Downloading file from url: {}".format(self.config.source_URL))
        if not os.path.exists(self.config.local_data_file):
            logger.info("File not found, downloading started...")
            filename, headers = request.urlretrieve(
                self.config.source_URL,
                self.config.local_data_file
            )
            logger.info(
                f"File: {filename} has been downloaded with following info: {headers}"
            )
        else:
            logger.info("File already exists")

    def extract_zip_file(self):
        try:
            logger.info("Extracting zip file...")
            os.makedirs(self.config.unzip_dir, exist_ok=True)
            if zipfile.is_zipfile(self.config.local_data_file):
                with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                    zip_ref.extractall(self.config.unzip_dir)
            else:
                logger.info("Not a zip file")
            logger.info(f"Data file extracted: {self.config.unzip_dir}")
        except Exception as e:
            raise e

