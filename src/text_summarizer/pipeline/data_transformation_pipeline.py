from text_summarizer.config.configuration_manager import ConfigurationManager
from text_summarizer.components.data_transformation import DataTransformation
from text_summarizer.logging import logger


class DataTransformationPipeline:
    def __init__(self):
        pass

    def run(self):
        logger.info("Data transformation pipeline started")
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.create_dataset()
        logger.info("Data transformation pipeline completed")


if __name__ == "__main__":
    try:
        pipeline = DataTransformationPipeline()
        pipeline.run()
    except Exception as e:
        logger.exception(e)
        raise e

