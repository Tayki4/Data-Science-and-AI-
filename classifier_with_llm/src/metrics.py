import numpy as np
import evaluate

_accuracy = evaluate.load('accuracy')

def compute_metrics(eval_pred):
    logits, lables = eval_pred
    preds = np.argmax(logits, axis=-1)
    
    return _accuracy.compute(
        predictions=preds, 
        references=lables
    )