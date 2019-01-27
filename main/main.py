import datetime
import sys
sys.path.append('..')
from db_api.db import DB
from logger.logger import Logger
from references.write_refs import WriteDicts as write_dicts
from constant import variables, headers

class WriteDB:
    def __init__(self, nameDB, rewrite=False):
        self.db = DB(nameDB)
        self.header = {'User-Agent': headers.headers[0]}
        self.write_dicts = write_dicts(headers=self.header)
        self.rewrite = rewrite

    def is_collection_empty(self, collection):
        i = collection.find()
        if(i.count()==0 or self.rewrite):
            return True
        return False

    def write_areas(self, name_collection):
        collection = self.db.get_collection(name_collection)
        if(self.is_collection_empty(collection)):
            self.write_dicts.write_areas(collection)

    def write_specs(self, name_collection):
        collection = self.db.get_collection(name_collection)
        if(self.is_collection_empty(collection)):
            self.write_dicts.write_spec(collection)

    def write_metro(self, name_collection):
        collection = self.db.get_collection(name_collection)
        if(self.is_collection_empty(collection)):
            self.write_dicts.write_metro(collection)

if __name__ == '__main__':
    date = datetime.datetime.now()
    today_date = '{0:%Y-%m}'.format(date)
    write_db = WriteDB('Parser-hh_ru')
    write_db.write_areas('regions_by_{}'.format(today_date))
    write_db.write_specs('specs_by_{}'.format(today_date))
    write_db.write_metro('metro_by_{}'.format(today_date))
