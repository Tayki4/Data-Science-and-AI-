import torch
from transformers import TrainingArguments, Trainer, DataCollatorWithPadding
from .metrics import compute_metrics
from .config import TrainConfig

def build_trainer(*, model, tokenizer, train_dataset, eval_dataset, cfg: TrainConfig):
    if cfg.gradient_checkpointing and hasattr(model, 'gradient_checkpointing_enable'):
        model.gradient_checkpointing_enable()
    
    args = TrainingArguments(
        output_dir=cfg.output_dir,
        seed=cfg.seed,
        num_train_epochs=cfg.num_train_epochs,
        learning_rate=cfg.lr,
        weight_decay=cfg.wd,
        per_device_train_batch_size=cfg.train_bs,
        per_device_eval_batch_size=cfg.eval_bs,
        gradient_accumulation_steps=cfg.gradient_accumulation_steps,
        warmup_ratio=cfg.warmup_ratio,
        logging_steps=cfg.logging_steps,
        evaluation_strategy='steps',
        eval_steps=cfg.eval_steps,
        save_strategy=cfg.save_strategy,
        save_steps=cfg.save_steps,
        save_total_limit=cfg.save_total_limit,
        load_best_model_at_end=True,
        metric_for_best_model='accuracy',
        greater_is_better=True,
        fp16=(cfg.fp16 and torch.cuda.is_available()),
        bf16=(cfg.bf16 and torch.cuda.is_available()),
        dataloader_num_workers=cfg.dataloader_num_works,
        dataloader_pin_memory=cfg.dataloader_pin_memory,
        report_to='none'
    )

    collator = DataCollatorWithPadding(tokenizer=tokenizer)

    return Trainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        tokenizer=tokenizer,
        data_collator=collator,
        compute_metrics=compute_metrics
    )