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


# returns string-formatted percent delta (+X or -X)
def deltaStr(percentLoss):
    percentLoss *= -1.0
    if (percentLoss < 0):
        return str(percentLoss)
    else:
        return "+" + str(percentLoss)


# returns tweet-formatted result
def formatResult(result):
    dl = round(result['download'] / 1000000.0, 1)
    ul = round(result['upload'] / 1000000.0, 1)
    pg = round(result['ping'], 1)

    download = str(dl) + " Mbps"
    upload = str(ul) + " Mbps"
    ping = str(pg) + " ms"
    ip = result['client']['ip']
    img = result['share']

    lossDown = float(expectDown) - dl
    lossUp = float(expectUp) - ul

    percentLossDown = deltaStr((lossDown / expectDown) * 100)
    percentLossUp = deltaStr((lossUp / expectUp) * 100)

    return """Paid for {0} down, {1} up.
    Down: {2} ({3}%)
    Up: {4} ({5}%)
    Ping: {6}
    IP: {7}""".format(expectDown, expectUp, download, percentLossDown, upload, percentLossUp, ping, ip)


# runs speed test, returns dictionary result
def testSpeed():
    print("testing speed...")
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    return s.results.dict()


# posts a tweet given text (TODO: and an optional image)
def postTweet(text):
    print("posting tweet...")
    result = api.PostUpdate(text)
    print("tweet result: " + str(result))
    # TODO: use more of Twitter's magic
    # https://python-twitter.readthedocs.io/en/latest/twitter.html#twitter.api.Api.PostUpdate
