import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        path = "C:/Users/2148389/PycharmProjects/OpenCartV1" +"\\logs\\" +"automation.log"
        logging.basicConfig(filename=path,format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger