import unittest
import sys
import pprint
sys.path.append('..')
from references.write_refs import WriteDicts
from db_api.db import DB
from constant import other_variables as vars


class db_test(unittest.TestCase):

    def setUp(self):
        self.db = DB(vars.db_name)
        self.collection = self.db.get_collection('specs_by_2018-10')

    # def test_write(self):
    #     doc = {'1':'kek', '7':'lol'}
    #     self.collection.insert_one(doc)

    def test_find(self):

        for i in self.collection.find():

            pprint.pprint(i)

if __name__=='__main__':
    unittest.main()
