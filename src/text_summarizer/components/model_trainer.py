import os
from text_summarizer.entity import ModelTrainerConfig
from transformers import TrainingArguments, Trainer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset, load_from_disk
from transformers import DataCollatorForSeq2Seq
import torch


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        # load dataset
        dataset = load_from_disk(str(self.config.data_path))

        trainer_args = TrainingArguments(
            output_dir=str(self.config.root_dir), num_train_epochs=self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy, eval_steps=self.config.eval_steps, save_steps=1e6,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )

        # trainer_args = TrainingArguments(
        #     output_dir=str(self.config.root_dir), num_train_epochs=0.1, warmup_steps=500,
        #     per_device_train_batch_size=1, per_device_eval_batch_size=1,
        #     weight_decay=0.01, logging_steps=10,
        #     evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
        #     gradient_accumulation_steps=16
        # )

        trainer = Trainer(
            model=model,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=data_collator,
            train_dataset=dataset["test"],
            eval_dataset=dataset["validation"],
        )
        trainer.train()

        model.save_pretrained(os.path.join(self.config.root_dir, "model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
