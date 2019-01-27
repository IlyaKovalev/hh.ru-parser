import sys
sys.path.append("..")
from logger.logger import Logger
from constant.constants import hh_ru_endpoints as ep
from make_req.handle_req import Request as request
from make_req.handle_req import ClientError, ServerError

class API:
    def __init__(self):
        self.logger = Logger.get_logger("vacancies_api")
        self.end_p = ep()
        self.url = self.end_p.hh_api() + self.end_p.hh_vacancies()
        self.request = request()

    def make_request(self, id='', params=None, headers=None):
        try:
            return self.request.make_request(self.url+id, params=params,).json()
        except (ClientError, ServerError):
            self.logger.error('Request error {} status code'.format(resp.status_code))
        except Exception:
            self.logger.error('error code: {} \n {}'.format(error_codes.json_err,Exception))
            raise
