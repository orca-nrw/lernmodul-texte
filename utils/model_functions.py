from utils import vis_functions as vf


def featurize(tweet):
    """Single word features"""

    return dict([(word, True) for word in tweet])


def supervised_classifier(tweets, nbclassifier, labels):
    """Supervised classifier"""

    print('#\tSoll\tIst\tPred\tTweet')

    negative = 0
    positive = 0
    error = 0
    for tweet in tweets.itertuples():

        prediction = nbclassifier.classify(featurize(tweet.Token))

        if tweet.Label != prediction:
            error += 1

        print('%i\t%s\t%s\t%s\t%.100s' % (tweet.Index, tweet.Label, prediction,
                                          (tweet.Label == prediction), tweet.Text.replace('\n', '')))

    print('\nGenauigkeit:', 1 - error / tweets.shape[0])


def unsupervised_classifier(tweets, kmclusterer, labels):
    """Unsupervised classifier"""

    print('#\tSoll\tIst\tPred\tTweet')

    negative = 0
    positive = 0
    error = 0
    for tweet in tweets.itertuples():

        prediction = kmclusterer.classify(tweet.Vector)

        if tweet.Label != labels[prediction]:
            error += 1

        print('%i\t%s\t%s\t%s\t%.100s' % (tweet.Index, tweet.Label, labels[prediction],
                                          (tweet.Label == labels[prediction]), tweet.Text.replace('\n', '')))

    print('\nGenauigkeit:', 1 - error / tweets.shape[0])
