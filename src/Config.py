import os
# https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv, find_dotenv

# Singleton Pattern
# Reference: https://python-patterns.guide/gang-of-four/singleton/
class Config:

    _dat = ""
    _sol = ""
    _url = ""

    _instance = None

    # TODO: Other configs and parameters might be included here

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.loadConfig()
            
        return cls._instance
        
    def loadConfig(self):
        # Load config from .env
        load_dotenv()

        self._dat = os.getenv('INSTANCES_DAT_PATH')
        self._sol = os.getenv('INSTANCES_SOL_PATH')
        self._url = os.getenv('INSTANCES_DAT_URL')

    @property
    def datPath(self):
        return self._dat  

    @property
    def solPath(self):
        return self._sol

    def printConfig(self):
        print(self._dat)
        print(self._sol)
        print(self._url)
