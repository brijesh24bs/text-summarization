import os
from pathlib import Path
from text_summarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self) -> bool:
        try:
            validation_data = None
            # load data
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            # validate data
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_data = False
                    with open(self.config.STATUS_FILE, "a") as f:
                        f.write(f"Validation failed for {file}\n")
                else:
                    validation_data = True
                    with open(self.config.STATUS_FILE, "a") as f:
                        f.write(f"Validation successful for {file}\n")
            return validation_data

        except Exception as e:
            raise e



