from lib import *


def main():
    result = testSpeed()
    tweet = formatResult(result)

    print tweet[0]
    print len(tweet[0])
    if (len(tweet[0]) <= 140):
        postTweet(*tweet)
        print("posted tweet.")
    else:
        print len(tweet[0])


if (__name__ == "__main__"):
    main()
