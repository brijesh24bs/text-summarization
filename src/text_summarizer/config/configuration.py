from text_summarizer.constants import *
from text_summarizer.utils.common import read_yaml, create_directories
from text_summarizer.entity import DataIngestionConfig
from pathlib import Path


class ConfigurationManager:
    def __init__(self, config_filepath: str = CONFIG_FILE_PATH, params_filepath: str = PARAMS_FILE_PATH):
        self.config = read_yaml(Path(config_filepath))
        self.params = read_yaml(Path(params_filepath))
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) :
        return self.config.data_ingestion





