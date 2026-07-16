import argparse
from .predictor import PredictorConfig, TextClassifier


def parse_args():
    p = argparse.ArgumentParser(
        description='AG_NEWS text classfication inference (end-user test)',
    )

    p.add_argument(
        '--model_dir',
        type=str,
        default='outputs/agnews_distilbert',
        help='Path to saved model directory.'
    )

    p.add_argument(
        '--text',
        type=str,
        nargs='+',
        default=None,
        help='One or more text inputs (batch mode). If omitted and --interactive is set, starts interactive mode.'
    )

    p.add_argument(
        '--interactive',
        action='store_true',
        help='Start interactive end-user test'
    )

    p.add_argument(
        '--device',
        type=str,
        default='cuda',
        help='Device selection'
    )

    p.add_argument(
        '--max_len',
        type=int,
        default=256,
        help='Tokenizer max lenght'
    )

    return p.parse_args()

def _pretty_print(text: str, label: str, conf: float):
    print(
        f'\n\n'
        f'Text: {text}\n\n'
        f'Pred: {label}\n\n'
        f'Coenf: {conf}\n\n'
    )

def interactive_loop(clf: TextClassifier):
    print(
        f'AG_NEWS END-USER Test\n'
        f'Type a news or paste it and press "enter"..!\n'
        f'For quiting --> send empty row, write q or quit..!\n'
    )

    while True:
        text = input('NEWS: ').strip()
        if not text or text.lower() in {'q', 'quit', 'exit'}:
            print('Application has been closing..!')
            break

        (orig, label, conf) = clf.predict([text])[0]

        _pretty_print(
            text=orig,
            label=label,
            conf=conf
        )

def main():
    args = parse_args()

    cfg = PredictorConfig(
        model_dir=args.model_dir,
        max_len=args.max_len,
        device=args.device
    )

    clf = TextClassifier(cfg=cfg)

    if args.interactive:
        interactive_loop(clf)
        return
    
    if not args.text:
        raise SystemExit('Exception: use --text or --interactive')
    
    results = clf.predict(texts=args.text)
    for text, label, conf in results:
        _pretty_print(
            text=text,
            label=label,
            conf=conf
        )
    
if __name__ == '__main__':
    main()