import speedtest
import settings


# {'client':
#   {'rating': '0', 'loggedin': '0', 'isprating': '3.7',
#     'ispdlavg': '0', 'ip': '67.189.31.203', 'isp': 'Comcast Cable',
#     'lon': '-123.1008', 'ispulavg': '0', 'country': 'US', 'lat': '44.0197'
#   },
#   'bytes_sent': 15769600, 'download': 76905445.7852311,
#   'timestamp': '2019-07-27T06:10:50.236057Z',
#   'share': u'http://www.speedtest.net/result/8450775228.png',
#   'bytes_received': 96571756, 'ping': 28.591, 'upload': 12193065.659968669,
#   'server': {
#     'latency': 28.591, 'name': 'Corvallis, OR',
#     'url': 'http://speedtest.peakinternet.com:8080/speedtest/upload.php',
#     'country': 'United States', 'lon': '-123.2760', 'cc': 'US',
#     'host': 'speedtest.peakinternet.com:8080', 'sponsor': 'PEAK Internet',
#     'url2': 'http://speedtest2.peakinternet.com/speedtest/upload.php',
#     'lat': '44.5708', 'id': '1159', 'd': 62.845870823467436
#   }}
def testSpeed():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    return s.results.dict()


def main():
    print("secret: " + str(settings.SECRET_TEST))
    result = testSpeed()
    print("download: " + str(result['download'] / 1000000.0) + "Mbps")
    print("upload: " + str(result['upload'] / 1000000.0) + "Mbps")
    print("ping: " + str(result['ping']))


if (__name__ == "__main__"):
    main()
