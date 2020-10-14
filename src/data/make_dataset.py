from src.common.sql_helpers.pipeline import SqlFeaturePipeline
from src.common.base import BaseHelpers
from sqlalchemy import create_engine
from decouple import config
import os


connection_string = config('ENGINE_PATH')
class MakeDatasetSql(BaseHelpers):
    def __init__(self, **kwargs):
        super(MakeDatasetSql, self).__init__(**kwargs)
        self.engine = create_engine(connection_string)
        self.pipeliner = SqlFeaturePipeline(self.engine)

    def make_dataset(self):
        self.pipeliner.import_scripts(os.path.join(config('PYTHONPATH'), "src/data/sql/"))
        self.pipeliner.run()

class MakeDataset(BaseHelpers): 
    def __init__(self, input_filepath, output_filepath, **kwargs): 
        """
        Arguments:
            input_filepath {str} -- filepath from PYTHONPATH
            output_filepath {str} -- filepath from PYTHONPATH
        """
        super(MakeDataset, self).__init__(**kwargs)
        self.input_filepath = os.path.join(config('PYTHONPATH'), input_filepath)
        self.output_filepath = os.path.join(config('PYTHONPATH'), output_filepath)

    def make_dataset(self):
        """ Runs data processing scripts to turn raw data from (../raw) into
            cleaned data ready to be analyzed (saved in ../processed).
        """
        self.log.info('making final data set from raw data')
        pass


if __name__ == '__main__':
#   data = MakeDatasetSql()
    data = MakeDataset('/data/raw/test.csv', '/data/processed/test.csv')
    data.make_dataset()