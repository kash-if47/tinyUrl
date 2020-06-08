import re
import unittest

from src.tinyUrl import TinyUrlConverter


class MyTestCase(unittest.TestCase):
    tinyUrl = TinyUrlConverter()
    domain = "http://localhost/"

    def test_generateTinyUrl(self):
        result = self.tinyUrl.generateUrl("https://www.t-mobile.com/cell-phone/samsung-galaxy-note10-plus-5g?sku=610214662927")
        self.assertEqual(result.startswith(self.domain), True)
        result = result.replace(self.domain, '')
        self.assertEqual(bool(re.match('^[a-z0-9]+$', result)), True)
        return result

    def test_randomGenerator(self):
        result = self.tinyUrl.randomKey(5)
        # print(result)
        self.assertEqual(bool(re.match('^[a-z0-9]+$', result)), True)

    def test_getLongUrl(self):
        result = self.test_generateTinyUrl()
        longUrl = self.tinyUrl.getLongUrl(result)
        self.assertEqual("https://www.t-mobile.com/cell-phone/samsung-galaxy-note10-plus-5g?sku=610214662927",longUrl)

    def test_duplicateUrl(self):
        result = self.test_generateTinyUrl()
        result2 = self.test_generateTinyUrl()
        self.assertEqual(result, result2)

    def test_tracker(self):
        key = self.test_generateTinyUrl()
        self.test_getLongUrl()
        self.test_getLongUrl()
        self.test_getLongUrl()
        tracking = self.tinyUrl.getTracking(key)
        self.assertEqual(tracking, 3)


if __name__ == '__main__':
    unittest.main()
