from text_summarizer.config.configuration_manager import ConfigurationManager
from text_summarizer.components.data_ingestion import DataIngestion
from text_summarizer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        try:
            logger.info("Data ingestion pipeline started")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logger.info("Data ingestion pipeline completed")

        except Exception as e:
            raise e

