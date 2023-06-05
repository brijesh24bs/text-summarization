from text_summarizer.components.model_evaluation import ModelEvaluation
from text_summarizer.config.configuration_manager import ConfigurationManager
from text_summarizer.logging import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        model_evaluation = ModelEvaluation(config.get_model_evaluation_config())
        model_evaluation.evaluate()


if __name__ == "__main__":
    try:
        pipeline = ModelEvaluationPipeline()
        pipeline.run()
    except  Exception as e:
        logger.exception(e)
        raise e