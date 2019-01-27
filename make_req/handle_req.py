import requests
import sys
import random
import subprocess
sys.path.append('..')
from logger.logger import Logger
from constant import error_codes
from constant.headers import headers

class ApiError(Exception):
    pass

class ServerError(ApiError):
    pass

class ClientError(ApiError):
    pass

class Request:
    def __init__(self):
        self.logger = Logger.get_logger(name="Request api")
        self.counter = random.randrange(1,10)
        self.header = headers[random.randrange(len(headers))]

    def change_chain(self):
        self.counter = random.randrange(1,10)
        subprocess.call(['systemctl','restart','tor'])
        self.header = headers[random.randrange(len(headers))]

    def make_request(self, url, params=None):
        resp = None
        proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
        }
        try:
            if(self.counter==0):
                self.change_chain()
            self.counter -= 1
            resp = requests.get(url, headers=self.header,
                                     params=params,
                                     proxies=proxies)
        except Exception:
            self.logger.error('error code: {} \n {}'.format(
            error_codes.bad_request,Exception))
            raise
        error_type = str(resp.status_code)[0]
        self.logger.info('resp status_code {}'.format(resp.status_code))
        if error_type == '5':
            raise ServerError
        if error_type == '4':
            raise ClientError
        if resp.status_code!=200:
            raise ApiError
        return resp
