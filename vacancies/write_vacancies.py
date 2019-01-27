import sys
sys.path.append('..')
from api import API
from logger.logger import Logger
from references.manager import Manager
from db_api.db import DB
from constant.variables import *

class Writer:
    def __init__(self):
        self.logger = Logger.get_logger("vacancies_writer")
        self.api = API()
        self.manager = Manager()
        self.db = DB(db_name=ov.db_name)
        self.collection = db.get_collection(vacancies)

    def write_vacancies(self, collection):
        areas = self.manager.get_areas()
        specs = self.manager.get_specs()
        f = open('Report', 'rw')
        area_id = f.readline()[0]
        spec_id = f.readline()[1]
        if area_id in areas:
            areas = areas[areas.index(area_id):]
        if spec_id in specs:
            specs = specs[areas.index(spec_id):]
        try:
            for area_key, area_value in areas.items():
                area_id = area_value
                vacancies_id = set()
                for spec_key, spec_value in specs.items():
                    result = {
                        'area': area_id,
                        'specialization': spec_value,
                        'vacancies':{}
                    }
                    for page in range(20):
                        spec_id = spec_value
                        params = {
                            'area': area_id,
                            'specialization': spec_id,
                            'date_from': date_from,
                            'per_page': 100,
                            'page': page
                        }
                        resp = self.api.make_request(params=params)
                        resp = dict(resp)
                        for item in resp['items']:
                            if int(item['id']) not in vacancies_id:
                                vacancies_id.add(int(item['id']))
                                collection.insert_one(dict(resp))
        except Exception:
            f.write('{} \n {}'.format(area_id, spec_id))
            f.close()
            raise
        f.close()
