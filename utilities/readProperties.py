import configparser
import os

config = configparser.RawConfigParser()
config.read("C:/Users/2148389/PycharmProjects/OpenCartV1/configurations/config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('commonInfo', 'email')
        return username

    @staticmethod
    def getPassword():

        password = config.get('commonInfo', 'baseURL')
        return password