from text_summarizer.entity import DataTransformationConfig
from transformers import AutoTokenizer
import datasets
import os


class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def get_tokens(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], truncation=True, max_length=1024)
        attention_masks = input_encodings['attention_mask']

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], truncation=True, max_length=128)

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_masks': attention_masks,
            'labels': target_encodings['input_ids']
        }

    def create_dataset(self):
        dataset_samsum = datasets.load_from_disk(str(self.config.data_path))
        dataset_samsum_transformed = dataset_samsum.map(self.get_tokens, batched=True)
        dataset_samsum_transformed.save_to_disk(os.path.join(self.config.root_dir, 'samsum_dataset'))
