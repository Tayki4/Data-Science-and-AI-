from dataclasses import dataclass

@dataclass(frozen=True)
class TrainConfig:
    model_name: str = 'distilbert-base-uncased'
    max_len: int = 256
    output_dir: str = 'outputs/agnews_distilbert'
    seed: int = 42
    num_train_epochs: int = 2
    lr: float = 2e-5
    wd: float = 0.01 # wd --> weight_decay
    train_bs: int = 16 # bs --> batch_size
    eval_bs: int = 32
    gradient_accumulation_steps: int = 1
    logging_steps: int = 200
    eval_steps: int = 2000
    save_steps: int = 2000
    evaluation_strategy: str = 'no'
    save_total_limit: int = 2
    load_best_model: bool = True
    metric_for_best_model: str = 'accuracy'
    greater_is_better: bool = True
    warmup_ratio: float = 0.06
    dataloader_num_works: int = 2
    dataloader_pin_memory: bool = True
    fp16: bool = True
    bf16: bool = False
    gradient_checkpointing: bool = False
    report_to: str = 'none'
    save_strategy: str = "steps"
