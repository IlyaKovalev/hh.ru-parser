from pymongo import MongoClient

class hh_ru_endpoints:

    def __init__(self):
        pass

    def hh_api(self):
        return 'https://api.hh.ru'

    def hh_vacancies(self):
        return '/vacancies'

    def hh_areas(self):
        return '/areas'

    def hh_spec(self):
        return '/specializations'

    def hh_metro(self):
        return '/metro'

    def area_id(self, area='Россия'):
        areas = {'countries':'countries','Россия':'113'}
        area_id = areas.get(area, None)
        if area_id is None:
            return ''
        return '/'+area_id



    def references_api(self):
        return
