import logging

class Logger:

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)

    def get_logger(self, name):
        return logging.getLogger(name)
