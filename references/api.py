import json
import sys
import pprint
sys.path.append('..')
from constant.constants import hh_ru_endpoints as ep
from constant import variables as ov
from constant import error_codes
from make_req.handle_req import Request as request
from logger.logger import Logger
from make_req.handle_req import ClientError, ServerError

class API:
    def __init__(self):
        self.ep = ep()
        self.log = Logger.get_logger(name="Reference api")
        self.request = request(self.log)

    def make_request(self, url):
        response = self.request.make_request(url)
        try:
            response = response.json()
            return response
        except (ClientError, ServerError):
            self.logger.error('Request error {} status code'.format(resp.status_code))
        except Exception:
            log.error('error code: {} \n {}'.format(error_codes.json_err,Exception))
            raise

    def get_area_dict(self):
        url = self.ep.hh_api() + self.ep.hh_areas() + self.ep.area_id()
        return self.make_request(url)

    def get_spec_dict(self):
        url = self.ep.hh_api() + self.ep.hh_spec()
        return self.make_request(url)

    def get_metro_dict(self):
        """This method GET list of all metro in all cities"""
        url = self.ep.hh_api() + self.ep.hh_metro()
        return self.make_request(url)
