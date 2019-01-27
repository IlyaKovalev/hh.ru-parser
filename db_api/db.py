from pymongo import MongoClient
import sys
sys.path.append('..')
from logger.logger import Logger


class DB:
    def __init__(self, db_name, host='localhost', port=27017):
        self.logging = Logger()
        self.logger = self.logging.get_logger(name='db status')
        self.client = self.connect_db(host, port)
        self.db = self.client[db_name]

    def connect_db(self, host, port):
        try:
            client = MongoClient(host, port, serverSelectionTimeoutMS=5)
            self.logger.info(client.server_info())
            return client
        except Exception:
            self.logger.error('can not connect to db')
            raise

    def get_collection(self, name):
        return self.db[name]
