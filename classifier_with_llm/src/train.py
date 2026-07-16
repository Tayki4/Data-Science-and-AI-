import os
import numpy as np
import torch
from transformers import AutoTokenizer
from .config import TrainConfig
from .data import load_agnews, get_label_info, tokenize_dataset
from .model import build_model
from .trainer_factory import build_trainer

def seed_everything(seed: int):
    torch.manual_seed(seed)
    np.random.seed(seed)

def run_training(cfg: TrainConfig):
    print(f'Cuda : {torch.cuda.is_available()}')
    if torch.cuda.is_available():
        print(f'GPU : {torch.cuda.get_device_properties(0)}')

    os.makedirs('outputs', exist_ok=True)
    seed_everything(cfg.seed)

    ds = load_agnews()
    
    label_names, num_labels, id2label, label2id = get_label_info(ds)

    tokenizer = AutoTokenizer.from_pretrained(cfg.model_name)

    ds_tok = tokenize_dataset(
        ds=ds, 
        tokenizer=tokenizer,
        max_len=cfg.max_len
    )

    print(ds_tok['train'].shape)
    print(ds_tok['test'].shape)

    model = build_model(
        model_name=cfg.model_name, 
        num_labels=num_labels, 
        id2label=id2label, 
        label2id=label2id
    )

    trainer = build_trainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=ds_tok['train'],
        eval_dataset=ds_tok['test'],
        cfg=cfg
    )

    trainer.train()
    metrics = trainer.evaluate()

    trainer.save_model(cfg.output_dir)
    tokenizer.save_pretrained(cfg.output_dir)

    return {
        'label_names': label_names,
        'metrics': metrics,
        'saved_to': cfg.output_dir
    }

def main():
    cfg = TrainConfig()
    result = run_training(cfg)
    print(
        f'Labels: {result["label_names"]}\n'
        f'Final Metrics: {result["metrics"]}\n'
        f'Saved to: {result["saved_to"]}'
    )

if __name__ == '__main__':
    main()