from utils import vis_functions as vf


def get_features_for_single_tweet(tweet):
    return dict([(word, True) for word in tweet])


def supervised_classifier(tweets, tweets_copy, nbclassifier, labels):
    """Supervised classifier"""

    print('#\tSoll\tIst\t∆\tTweet')

    negative = 0
    positive = 0
    error = 0
    for tweet in tweets.itertuples():

        features = get_features_for_single_tweet(tweet.Token)
        prediction = nbclassifier.classify(features)

        if tweet.Label != prediction:
            delta = 'X'
            error += 1
        else:
            delta = ' '

        if prediction == 'negativ':
            negative += 1

        else:
            positive += 1

        print('%i\t%s\t%s\t%s\t%.100s' % (tweet.Index, tweet.Label, prediction,
                                          delta, tweets_copy.iloc[tweet.Index].replace('\n', '')))

    print('\nGenauigkeit:', 1 - error / tweets.shape[0])
    vf.plot_pie([negative, positive], labels=labels)


def unsupervised_classifier(tweets, tweets_copy, kmclusterer, labels):
    """Unsupervised classifier"""

    print('#\tSoll\tIst\t∆\tTweet')

    negative = 0
    positive = 0
    error = 0
    for tweet in tweets.itertuples():

        prediction = kmclusterer.classify(tweet.Vector)

        if prediction == 0:
            cluster = 'negativ'
            negative += 1

        else:
            cluster = 'positiv'
            positive += 1

        if tweet.Label != cluster:
            delta = 'X'
            error += 1

        else:
            delta = ' '

        print('%i\t%s\t%s\t%s\t%.100s' % (tweet.Index, tweet.Label, cluster,
                                          delta, tweets_copy.iloc[tweet.Index].replace('\n', '')))

    print('\nGenauigkeit:', 1 - error / tweets.shape[0])
    vf.plot_pie([negative, positive], labels=labels)
