import speedtest
import settings
import twitter

api = twitter.Api(
    consumer_key=settings.API_KEY,
    consumer_secret=settings.API_SECRET,
    access_token_key=settings.ACCESS_TOKEN,
    access_token_secret=settings.ACCESS_SECRET
)
expectDown = float(settings.EXPECTED_DOWN_MBPS)
expectUp = float(settings.EXPECTED_UP_MBPS)
DEBUG = settings.DEBUG

isps = {
    "Comcast Cable": {
        "name": "Xfinity",
        "handles": [
            "@Xfinity",
            "@ComcastCares"
        ]
    }
}

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

# returns string-formatted percent delta (+X or -X)
def deltaStr(percentLoss):
    percentLoss *= -1.0
    if (percentLoss < 0):
        return str(percentLoss)
    else:
        return "+" + str(percentLoss)


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

# returns tweet-formatted result as tuple (text, image)
def formatResult(result):
    result = normalizeResults(result)

    download = str(result.dl) + " Mbps"
    upload = str(result.ul) + " Mbps"
    ping = str(result.pg) + " ms"
    
    text = """Paid for {0} down, {1} up from {8}.
Down: {2} ({3}%)
Up: {4} ({5}%)
Ping: {6}
IP: {7}
{9}""".format(expectDown, 
        expectUp, 
        download, 
        deltaStr(result.percentLossDown), 
        upload, 
        deltaStr(result.percentLossUp), 
        ping, 
        result.ip, 
        result.isp['handles'][0], 
        result.isp['handles'][1]
    )

    return (text, result.img)


# runs speed test, returns dictionary result
def testSpeed():
    print("testing speed...")
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    return s.results.dict()

def shouldTweet(result):
    result = normalizeResults(result)
    if (result.percentLossDown > float(settings.THRESHOLD_PERCENT_LOSS)):
        return True
    return False

# posts a tweet given text and an image URL
def postTweet(text, image=None):
    print("posting tweet...")
    result = api.PostUpdate(text, image)
    print("tweet result: " + str(result))
    # TODO: use more of Twitter's magic
    # https://python-twitter.readthedocs.io/en/latest/twitter.html#twitter.api.Api.PostUpdate
