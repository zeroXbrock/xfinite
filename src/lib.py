import speedtest
import settings
import twitter
from helpers import *

api = twitter.Api(
    consumer_key=settings.API_KEY,
    consumer_secret=settings.API_SECRET,
    access_token_key=settings.ACCESS_TOKEN,
    access_token_secret=settings.ACCESS_SECRET
)

DEBUG = settings.DEBUG

class Result:
    def __init__(self, t):
        (dl, ul, pg, lossDown, percentLossDown, lossUp, percentLossUp, ip, img, isp) = t
        self.dl = dl
        self.img = img
        self.ip = ip
        self.isp = isp
        self.lossDown = lossDown
        self.lossUp = lossUp
        self.percentLossDown = percentLossDown
        self.percentLossUp = percentLossUp
        self.pg = pg
        self.ul = ul

def normalizeResults(result):
    dl = round(result['download'] / 1000000.0, 1)
    ul = round(result['upload'] / 1000000.0, 1)
    pg = round(result['ping'], 1)
    lossDown = expectDown - dl
    lossUp = expectUp - ul
    ip = result['client']['ip']
    img = result['share']
    isp = isps[result['client']['isp']]
    percentLossDown = (lossDown / expectDown) * 100
    percentLossUp = (lossUp / expectUp) * 100

    return Result((dl, ul, pg, lossDown, percentLossDown, lossUp, percentLossUp, ip, img, isp))

# runs speed test, returns dictionary result
def testSpeed():
    print("testing speed...")
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    return s.results.dict()

# posts a tweet given text and an image URL
def postTweet(text, image=None):
    print("posting tweet...")
    result = api.PostUpdate(text, image)
    print("tweet result: " + str(result))
    # TODO: use more of Twitter's magic
    # https://python-twitter.readthedocs.io/en/latest/twitter.html#twitter.api.Api.PostUpdate
