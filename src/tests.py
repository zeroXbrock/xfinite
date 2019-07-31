import json
from collections import namedtuple
import helpers
import unittest

def _json_object_hook(d): 
    return namedtuple('X', d.keys())(*d.values())

def json_to_obj(data): 
    return json.loads(data, object_hook=_json_object_hook)
# thanks https://stackoverflow.com/a/15882054/1438589

mock_result_85_down_str = '{"dl": 84.6, "img": "http^^^//www.speedtest.net/result/8461794947.png", "ul": 12.3, "ip": "67.189.31.203", "isp": {"handles": ["@Xfinity", "@ComcastCares"], "name": "Xfinity"}, "lossDown": 115.4, "percentLossUp": -23.000000000000007, "percentLossDown": 57.70000000000001, "lossUp": -2.3000000000000007, "pg": 30.1}'
#mock_85_down = namedtuple(mock_85_down_str)
mock_result_85_down = json_to_obj(mock_result_85_down_str)

class TestHelpers(unittest.TestCase):
    def it_should_tweet_past_threshold(self):
        self.assertTrue(helpers.shouldTweet(mock_result_85_down))

if __name__ == '__tests__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestLib)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main(TestHelpers)