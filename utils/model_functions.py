from utils import vis_functions as vf


def featurize(tweet):
    """Get single word features as dictionary"""

    return dict([(word, True) for word in tweet])


def classify_supervised_multiple(tweets, classifier, labels):
    """Predict sample tweets by supervised classifier and calculate accuracy"""

    print('#\tSoll\tIst\tPrognose Tweet')

    error = 0
    for tweet in tweets.itertuples():

        prediction = classifier.classify(featurize(tweet.Token))

        if tweet.Label != prediction:
            error += 1

        print('%i\t%s\t%s\t%s\t %.100s' % (tweet.Index, tweet.Label, prediction,
                                           (tweet.Label == prediction), tweet.Text.replace('\n', '')))

    print('\nGenauigkeit:', 1 - error / tweets.shape[0])


def classify_unsupervised_multiple(tweets, classifier, labels):
    """Predict sample tweets by unsupervised classifier and calculate accuracy"""

    print('#\tSoll\tIst\tPrognose Tweet')

    error = 0
    for tweet in tweets.itertuples():

        prediction = classifier.classify(tweet.Vector)

        if tweet.Label != labels[prediction]:
            error += 1

        print('%i\t%s\t%s\t%s\t %.100s' % (tweet.Index, tweet.Label, labels[prediction],
                                           (tweet.Label == labels[prediction]), tweet.Text.replace('\n', '')))

    print('\nGenauigkeit:', 1 - error / tweets.shape[0])
