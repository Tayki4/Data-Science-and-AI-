from dataclasses import dataclass
from typing import List, Tuple
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

@dataclass(frozen=True)
class PredictorConfig:
    model_dir: str
    max_len: int = 256
    device: str = 'cuda'


class TextClassifier:
    def __init__(self, cfg: PredictorConfig):
        self.cfg = cfg
        self.device = self.cfg.device
        self.tokenizer = AutoTokenizer.from_pretrained(cfg.model_dir)
        self.model = AutoModelForSequenceClassification.from_pretrained(cfg.model_dir)
        self.model.to(self.device)
        self.model.eval()
    
    @torch.no_grad()
    def predict(self, texts: List[str]) -> List[Tuple[str, str, float]]:
        if not texts:
            return []
        
        enc = self.tokenizer(
            texts,
            truncation=True,
            max_length=self.cfg.max_len,
            padding=True,
            return_tensors='pt',
        ).to(self.device)

        logits = self.model(**enc).logits
        probs = torch.softmax(logits, dim=-1)
        confs, pred_ids = torch.max(probs, dim=-1)

        pred_ids = pred_ids.detach().cpu().tolist()
        confs= confs.detach().cpu().tolist()

        id2label = self.model.config.id2label
        labels = [id2label[i] for i in pred_ids]

        return list(zip(texts, labels, confs))