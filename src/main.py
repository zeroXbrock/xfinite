from lib import *


def main():
    result = testSpeed()
    tweet = formatResult(result)

    print tweet[0]
    if (DEBUG):
        print len(tweet[0])

    if (len(tweet[0]) <= 140):
        if (not DEBUG):
            postTweet(*tweet)
        print("posted tweet.")
    else:
        print "tweet too long: " + str(len(tweet[0]))


if (__name__ == "__main__"):
    main()
