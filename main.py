from text_summarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from text_summarizer.pipeline.data_validation_pipeline import DataValidationPipeline
from src.text_summarizer.logging import logger

data_ingestion_pipeline = DataIngestionTrainingPipeline()
data_ingestion_pipeline.run()

data_validation_pipeline = DataValidationPipeline()
data_validation_pipeline.run()
