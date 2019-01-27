

import unittest
import sys
sys.path.append('..')
from references.api import API
from logger.logger import Logger

class dict_test(unittest.TestCase):

    def setUp(self):
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X \
            10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.logging = Logger('test refs api')
        self.logger = self.logging.get_logger()
        self.api = API(self.logger, self.header)

    def test_make_request(self):
        url = 'https://api.hh.ru/specializations'
        #resp = self.api.make_request(url)
        #print(len(resp))

    def test_getSpec(self):
        resp = self.api.get_spec_dict()
        self.assertEqual(len(resp), 28)

if __name__=='__main__':
    unittest.main()
