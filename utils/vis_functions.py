import numpy as np
import matplotlib.pyplot as plt


def plot_tweet_length_distribution(tweets_length):
    """Count tokens per tweet and plot their length distribution."""

    y, x, _ = plt.hist(tweets_length, np.max(tweets_length))
    plt.xlabel('Words per tweet')
    plt.ylabel('Amount of tweets')
    plt.title('Tweet length distribution')
    plt.plot(x[np.where(y == y.max())], y.max(), 'ro')
    plt.legend(np.round(x[np.where(y == y.max())]))
    plt.show()


def plot_clusters(means):
    """Plot clusters"""

    min_neg = np.min(means[0])
    max_pos = np.max(means[1])
    plt.fill_between([min_neg, 0], [0, min_neg], alpha=0.5)
    plt.fill_between([0, max_pos], [max_pos, 0], alpha=0.5)
    plt.scatter(means[0], means[0])
    plt.scatter(means[1], means[1])
    plt.legend(['Negativ', 'Positiv', 'Negativ', 'Positiv'])


def plot_image(image, title):
    """Plot image"""

    plt.imshow(image, interpolation='bilinear')
    plt.title(title)
    plt.show()


def plot_pie(inputs, labels):
    plt.pie(inputs, labels=labels, autopct='%1.1f%%')
    plt.title('Stimmungsbild')
    plt.show()
