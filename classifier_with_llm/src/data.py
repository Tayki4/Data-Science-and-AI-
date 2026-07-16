from datasets import load_dataset
from transformers import PreTrainedTokenizerBase

def load_agnews():
    return load_dataset('ag_news')


def get_label_info(ds):
    labels_names = ds['train'].features['label'].names

    # labels_names = ['World', 'Sports', 'Business', 'Sci/Tech'] 


    id2label = {i: n for i, n in enumerate(labels_names)}

    # {
    #     0: 'World',
    #     1: 'Sports',
    #     2: 'Business',
    #     3: 'Sci/Tech'
    # }

    label2id = {n: i for i, n in enumerate(labels_names)}

    # {
    #     'World': 0,
    #     'Sports': 1,
    #     'Business': 2,
    #     'Sci/Tech: 3'
    # }

    return labels_names, len(labels_names), id2label, label2id

def tokenize_dataset(ds, tokenizer: PreTrainedTokenizerBase, max_len: int):
    def tokenize_fn(batch):
        return tokenizer(batch['text'], truncation=True, max_length=max_len)
    
    ds_tok = ds.map(tokenize_fn, batched=True, remove_columns=['text'])
    ds_tok.set_format(type='torch')

    # {
    #     'input_ids': [....],
    #     'attenon_mask': [...],
    #     'label': ...
    # }
    return ds_tok
