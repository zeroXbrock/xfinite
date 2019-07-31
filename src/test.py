import json
from collections import namedtuple
import lib
import unittest


def _json_object_hook(d): 
    return namedtuple('X', d.keys())(*d.values())

def json_to_obj(data): 
    return json.loads(data, object_hook=_json_object_hook)
# thanks https://stackoverflow.com/a/15882054/1438589



mock_result_85_down_str = '{"dl": 84.6, "img": "http^^^//www.speedtest.net/result/8461794947.png", "ul": 12.3, "ip": "67.189.31.203", "isp": {"handles": ["@Xfinity", "@ComcastCares"], "name": "Xfinity"}, "lossDown": 115.4, "percentLossUp": -23.000000000000007, "percentLossDown": 57.70000000000001, "lossUp": -2.3000000000000007, "pg": 30.1}'
#mock_85_down = namedtuple(mock_85_down_str)
mock_result_85_down = json_to_obj(mock_result_85_down_str)

class TestShouldTweet(unittest.TestCase):
    def test_upper(self):
        self.assertTrue(True)
