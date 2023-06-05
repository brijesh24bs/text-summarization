from  text_summarizer.config.configuration_manager import ConfigurationManager
from text_summarizer.components.data_validation import DataValidation
from text_summarizer.logging import logger


class DataValidationPipeline:
    def __init__(self):
        pass

    def run(self):
        logger.info("Data validation pipeline started")
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_data()
        logger.info("Data validation pipeline completed")


if __name__ == "__main__":
    try:
        pipeline = DataValidationPipeline()
        pipeline.run()
    except Exception as e:
        logger.exception(e)
        raise e

