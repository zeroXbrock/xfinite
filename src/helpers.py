import settings

expectDown = float(settings.EXPECTED_DOWN_MBPS)
expectUp = float(settings.EXPECTED_UP_MBPS)

isps = {
    "Comcast Cable": {
        "name": "Xfinity",
        "handles": [
            "@Xfinity",
            "@ComcastCares"
        ]
    }
}

# returns string-formatted percent delta (+X or -X)
def deltaStr(percentLoss):
    percentLoss *= -1.0
    if (percentLoss < 0):
        return str(percentLoss)
    else:
        return "+" + str(percentLoss)

# returns tweet-formatted result as tuple (text, image)
def formatResult(result):
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

def shouldTweet(result):
    if (result.percentLossDown > float(settings.THRESHOLD_PERCENT_LOSS)):
        return True
    return False