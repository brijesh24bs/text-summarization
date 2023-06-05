from text_summarizer.config.configuration_manager import ConfigurationManager
from text_summarizer.components.model_trainer import ModelTrainer
from text_summarizer.logging import logger

import unittest


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
            logger.info("Starting model training pipeline")
            config = ConfigurationManager()
            model_training_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(model_training_config)
            model_trainer.train()
            logger.info("Model training pipeline completed")


if __name__ == "__main__":
    try:
        pipeline = ModelTrainingPipeline()
        pipeline.run()
    except Exception as e:
        logger.exception(e)
        raise e
