import json
import glob
import pandas as pd


def load_json():
    """Load JSON"""

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
    """Format vocabulary"""

    vocab[['Wort', 'Typ']] = vocab['Wort'].str.split('|', 1, expand=True)
    vocab['Deklination'] = vocab['Deklination'].replace(regex={r'\r': ''})
    vocab['Merged'] = vocab['Wort'] + ',' + vocab['Deklination']
    vocab['Merged'] = vocab['Merged'].str.split(',')
    vocab = vocab.explode('Merged')
    vocab = vocab.sort_values('Wort').reset_index(drop=True)
    vocab = vocab.rename(columns={'Wort': 'Stamm', 'Merged': 'Wort'})
    vocab = vocab.drop(['Deklination'], axis=1)

    return vocab


def filter_vocabulary(vocab, sentiment, word):
    """Filter vocabulary"""

    nouns = vocab[(vocab['Stimmung'] == sentiment) & (
        vocab['Typ'] == word)]

    if sentiment == 'negativ':
        return pd.Series(nouns.Wert.values * (-100), index=nouns.Stamm).to_dict()

    else:
        return pd.Series(nouns.Wert.values * 100, index=nouns.Stamm).to_dict()


def process_emojis(tweets):
    """Process emojis"""

    positive_emojis = [r'🙂']
    for emoji in positive_emojis:
        tweets.replace(regex={emoji: 'gut'}, inplace=True)

    negative_emojis = [r'😟']
    for emoji in negative_emojis:
        tweets.replace(regex={emoji: 'schlecht'}, inplace=True)

    return tweets


def process_strings(tweets):
    """Process strings"""

    expressions = [
        r'@\S+',  # Find username
        r'http\S+',  # Find URL
        r'\n']  # Find new line

    for expression in expressions:
        tweets.replace(regex={expression: ''}, inplace=True)

    return tweets


def process_symbols(tweets):
    """Process symbols"""

    expression = '[^a-zA-ZäöüßÄÖÜ\s]'

    tweets.replace(regex={expression: ''}, inplace=True)

    return tweets
