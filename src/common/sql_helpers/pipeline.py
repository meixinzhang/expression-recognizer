from src.common.base import BaseHelpers
from collections import OrderedDict
from decouple import config
import sqlite3
import os
import time


class SqlFeaturePipeline(BaseHelpers):
    """
        Facilitates feature engineering using SQL
    """
    def __init__(self, engine, **kwargs):
        super(SqlFeaturePipeline, self).__init__(**kwargs)
        self.engine = engine
        self.files = OrderedDict() #

    def run(self):
        """
            Description:
                Run feature engineering pipeline
        :return:
        """

        for file in sorted(self.files.keys()):
            self.log.debug(f'Execution file: {file}')
            for query in self.files[file].split(";"):
                if len(query.strip()) > 0:
                    self.log.info(f"Executing query ({file}): \n{query}")
                    result = self.engine.execute(query)
                    self.log.info(f'Result: {result}')
                print('\n')

    def import_scripts(self, scripts_path):
        """ Load scripts from path into the environment """
        eng_scripts = sorted(os.listdir(scripts_path))
        for root, dirs, files in os.walk(scripts_path, topdown=True):
            print(files)
            for file in files:
                path = os.path.join(root, file)
                if path.endswith(".sql"):
                    with open(path, "r") as f:
                        self.files.update({path: f.read()})
        self.log.debug(f'Imported files ({len(self.files)}): {eng_scripts}')