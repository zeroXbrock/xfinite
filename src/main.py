from lib import *
from helpers import *

SPEED_OK = 1

def main():
    result = normalizeResults(testSpeed())
    if (not shouldTweet(result)):
        exit(SPEED_OK)
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
