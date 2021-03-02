import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def plot_tweets_per_year(twitter):
    """Plot tweets based on date of creation"""

    twitter['year'] = pd.to_datetime(twitter['created_at']).dt.year
    twitter['year'].value_counts().plot(kind='bar', title='Tweets created')
    return twitter


def plot_tweets_per_length(tweets_length):
    """Plot length distribution of tweets"""

    y, x, _ = plt.hist(tweets_length, np.max(tweets_length))
    plt.xlabel('Words per tweet')
    plt.ylabel('Counts')
    plt.title('Tweet length distribution')
    plt.plot(x[np.where(y == y.max())], y.max(), 'ro')
    plt.legend(np.round(x[np.where(y == y.max())]))
    plt.show()


def plot_clusters(centroids):
    """Plot cluster based on centroids"""

    min_neg = np.min(centroids[0])
    max_pos = np.max(centroids[1])
    plt.fill_between([min_neg, 0], [0, min_neg], alpha=0.5)
    plt.fill_between([0, max_pos], [max_pos, 0], alpha=0.5)
    plt.scatter(centroids[0], centroids[0])
    plt.scatter(centroids[1], centroids[1])
    plt.legend(['Negativ', 'Positiv', 'Negativ', 'Positiv'])


def plot_image(image, title):
    """Plot image with title"""

    plt.imshow(image, interpolation='bilinear')
    plt.title(title)
    plt.show()


def plot_pie(inputs, labels, title):
    """Plot pie chart with labels and title"""

    plt.pie(inputs, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.show()
