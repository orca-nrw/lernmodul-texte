import json
import glob
import pandas as pd


def load_stop_words():
    """Load stop words"""
    return pd.read_csv('./data/vocab/stop_words.txt', names=['Wort'])


def load_vocabulary(sentiment):
    """Load vocabulary"""

    vocab = pd.read_csv('./data/vocab/' + sentiment + 'e_words.txt', lineterminator='\n',
                        sep='\t', header=0, names=['Wort', 'Wert', 'Deklination'])
    vocab['Stimmung'] = sentiment
    return vocab


def load_json():
    files = []  # JSON
    for f in glob.glob("./data/tweets/*.json"):
        with open(f, "rb") as infile:
            files.append(json.load(infile))
            infile.close()
    return files
