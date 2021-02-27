import json
import glob
import pandas as pd


def load_json():
    files = []  # JSON
    for f in glob.glob("./data/tweets/*.json"):
        with open(f, "rb") as infile:
            files.append(json.load(infile))
            infile.close()
    return files


def load_stop_words():
    """Load stop words"""
    return pd.read_csv('./data/vocab/stop_words.txt', names=['Wort'])


def load_vocabulary(sentiment):
    """Load vocabulary"""

    vocab = pd.read_csv('./data/vocab/' + sentiment + 'e_words.txt', lineterminator='\n',
                        sep='\t', header=0, names=['Wort', 'Wert', 'Deklination'])
    vocab['Stimmung'] = sentiment
    return vocab


def format_vocabulary(vocab):

    vocab[['Wort', 'Typ']] = vocab['Wort'].str.split('|', 1, expand=True)

    vocab['Deklination'] = vocab['Deklination'].replace(regex={r'\r': ''})

    vocab['Merged'] = vocab['Wort'] + ',' + vocab['Deklination']
    vocab['Merged'] = vocab['Merged'].str.split(',')
    vocab = vocab.explode('Merged')
    vocab = vocab.sort_values('Wort').reset_index(drop=True)
    vocab = vocab.rename(columns={'Wort': 'Stamm', 'Merged': 'Wort'})
    vocab = vocab.drop(['Deklination'], axis=1)

    return vocab


def process_emojis(tweets):

    positive_emojis = [r'🙂']
    for emoji in positive_emojis:
        tweets.replace(regex={emoji: 'gut'}, inplace=True)

    negative_emojis = [r'😟']
    for emoji in negative_emojis:
        tweets.replace(regex={emoji: 'schlecht'}, inplace=True)

    return tweets


def process_strings(tweets):

    expressions = [
        r'@\S+',  # Find username
        r'http\S+',  # Find URL
        r'\n']  # Find new line

    for expression in expressions:
        tweets.replace(regex={expression: ''}, inplace=True)

    return tweets


def process_symbols(tweets):

    expression = '[^a-zA-ZäöüßÄÖÜ\s]'

    tweets.replace(regex={expression: ''}, inplace=True)

    return tweets
