import json
import glob
import pandas as pd


def load_json():
    """Load JSON as list"""

    files = []  # JSON
    for f in glob.glob("./data/tweets/*.json"):
        with open(f, "rb") as infile:
            files.append(json.load(infile))
            infile.close()
    return files


def load_stop_words():
    """Load stop words as DataFrame"""

    return pd.read_csv('./data/vocabulary/stop_words.txt', names=['Wort'])


def load_vocabulary(sentiment):
    """Load vocabulary as DataFrame"""

    vocabulary = pd.read_csv('./data/vocabulary/' + sentiment + 'e_words.txt', lineterminator='\n',
                             sep='\t', header=0, names=['Wort', 'Wert', 'Deklination'])
    vocabulary['Stimmung'] = sentiment
    return vocabulary


def format_vocabulary(vocabulary):
    """Format vocabulary"""

    vocabulary[['Wort', 'Typ']] = vocabulary['Wort'].str.split(
        '|', 1, expand=True)
    vocabulary['Deklination'] = vocabulary['Deklination'].replace(regex={
                                                                  r'\r': ''})
    vocabulary['Merged'] = vocabulary['Wort'] + ',' + vocabulary['Deklination']
    vocabulary['Merged'] = vocabulary['Merged'].str.split(',')
    vocabulary = vocabulary.explode('Merged')
    vocabulary = vocabulary.sort_values('Wort').reset_index(drop=True)
    vocabulary = vocabulary.rename(columns={'Wort': 'Stamm', 'Merged': 'Wort'})
    vocabulary = vocabulary.drop(['Deklination'], axis=1)

    return vocabulary


def filter_vocabulary(vocabulary, sentiment, word):
    """Filter vocabulary based on sentiment and word type"""

    nouns = vocabulary[(vocabulary['Stimmung'] == sentiment) & (
        vocabulary['Typ'] == word)]

    if sentiment == 'negativ':
        return pd.Series(nouns.Wert.values * (-100), index=nouns.Stamm).to_dict()

    else:
        return pd.Series(nouns.Wert.values * 100, index=nouns.Stamm).to_dict()


def process_emojis(tweets):
    """Process emojis based on sentiment"""

    positive_emojis = [r'🙂', r'😊', r'😛']
    for emoji in positive_emojis:
        tweets.replace(regex={emoji: 'gut'}, inplace=True)

    negative_emojis = [r'😟', r'😕', r'😩']
    for emoji in negative_emojis:
        tweets.replace(regex={emoji: 'schlecht'}, inplace=True)

    return tweets


def process_strings(tweets):
    """Process strings based on regular expressions"""

    expressions = [
        r'@\S+',  # Find username
        r'http\S+',  # Find URL
        r'\n',  # Find new line
    ]

    for expression in expressions:
        tweets.replace(regex={expression: ''}, inplace=True)

    return tweets


def process_symbols(tweets):
    """Process symbols based on regular expressions"""

    expression = '[^a-zA-ZäöüßÄÖÜ\s]'

    tweets.replace(regex={expression: ''}, inplace=True)

    return tweets
