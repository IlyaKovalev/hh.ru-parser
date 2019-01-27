import sys
sys.path.append('..')
from references.api import API
from logger.logger import Logger

class WriteDicts:

    def __init__(self):
        self.logging = Logger()
        self.logger = self.logging.get_logger('WriteDicts')
        self.api = API(self.logger)

    def write_areas(self, collection):
        areas = self.api.get_area_dict()
        collection.insert_one(dict(areas))
        self.logger.info('areas write: success')

    def write_spec(self, collection):
        specs = self.api.get_spec_dict()
        collection.insert_many([{str(i):specs[i] for i in range(len(specs))}])
        self.logger.info('specializations write: success')

    def write_metro(self, collection):
        metro = self.api.get_metro_dict()
        collection.insert_many([{str(i):metro[i] for i in range(len(metro))}])
        self.logger.info('metro write: success')
