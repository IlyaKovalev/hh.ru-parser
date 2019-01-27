import unittest
import sys
sys.path.append('..')
from vacancies.api import API
from logger.logger import Logger

class vacancies_api_test(unittest.TestCase):

    def setUp(self):
        self.header = {'User-Agent': 'Mozilla/5'}
        self.logging = Logger()
        self.logger = self.logging.get_logger('test refs api')
        self.api = API(self.logger)

    def test_make_request(self):
        url = 'https://api.hh.ru/specializations'
        #resp = self.api.make_request(url)

    def test_getSpec(self):
        print(self.api.make_request(headers=self.header)).status_code
        #resp = self.api.get_spec_dict()
        #self.assertEqual(len(resp), 28)

if(__name__=='__main__'):
    unittest.main()
