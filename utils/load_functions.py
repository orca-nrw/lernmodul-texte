import pandas as pd


def load_vocabulary(sentiment):
    """Load vocabulary"""

    vocab = pd.read_csv('./data/vocab/' + sentiment + 'e_words.txt', lineterminator='\n',
                        sep='\t', header=0, names=['Wort', 'Wert', 'Deklination'])
    vocab['Stimmung'] = sentiment
    return vocab
