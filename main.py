from lib import *


def main():
    result = testSpeed()
    tweet = formatResult(result)

    print tweet
    if (len(tweet) <= 140):
        postTweet(tweet)


if (__name__ == "__main__"):
    main()
