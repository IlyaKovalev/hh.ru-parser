import pprint
import sys
sys.path.append('..')

from logger.logger import Logger
from db_api.db import DB
from constant.variables import *

class Manager:
    def __init__(self):
        self.db = DB(db_name=vars.db_name)
        self.logger = Logger.get_logger("References_db_manager")

    def get_metro(self):
        return self.db.get_collection(name = ref_metro + date_from)

    def get_areas(self):
        collection = self.db.get_collection(name = ref_areas + date_from)
        data = collection.find_one()
        data = data.get('areas')
        regions = {}
        for d in data:
            regions[d.get('name')] = d.get('id')
        return regions

    def get_specs(self):
        collection = self.db.get_collection(name = ref_spec + date_from)
        data = collection.find()[0]
        count = len(data)
        self.logger.debug("specs count: {} \n data={}".format(count, data))
        specs = {}
        for key, value in data.items():
            if key!='_id':
                specs[key] = value.get('id')
        return specs
