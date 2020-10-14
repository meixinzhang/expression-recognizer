import unittest
from src.common.sql_helpers.pipeline import SqlFeaturePipeline
from sqlite3 import OperationalError
from decouple import config
import pandas as pd
import sqlite3
import os


PATH_CACHE = os.path.join(config('PYTHONPATH'), 'cache')

class SQLPipelineTester(unittest.TestCase):

    q1 = """
    drop table if exists feedback;
    
    create table feedback (
        name varchar primary key,
        text varchar
    );
    
    insert into feedback values
        ('Vitalii Dodonov', 'Vitalii is awesome!'),
        ('Brydon Parker', 'Brydon is great!'),
        ('Maxine Zhang', 'Maxine is fantastic!')
    """

    q2 = """
        select * from feedback
    """

    q3 = """
        selec1t from feedback
    """

    path = os.path.join(PATH_CACHE, 'sql_scripts')
    if not os.path.exists(path):
        os.makedirs(path)

    with open(os.path.join(path, '1.0 Create Table.sql'), 'w') as f:
        f.write(q1)
    with open(os.path.join(path, '2.0 Delete Table.sql'), 'w') as f:
        f.write(q2)

    engine = sqlite3.connect(os.path.join(PATH_CACHE, 'sqlite.db'))
    # engine = create_connection(os.path.join(PATH_CACHE, 'sqlite.db'))
    sfp = SqlFeaturePipeline(engine=engine, scritps_path=path, log_level='CRITICAL')

    def test_1a_read_sql_files(self):
        """ Test that files are imported successfully """
        self.sfp.import_scripts(scripts_path=self.path)
        assert len(self.sfp.files) == 2

    def test_2a_execution(self):
        """ Execute scripts sequentially  """
        self.sfp.run()

    def test_2b_execute_broken_query(self):
        """ Execute broken query - ensure that error is thrown  """
        try:
            self.engine.execute(self.q3)
            raise Exception
        except OperationalError:
            pass

    def test_3a_tables_created(self):
        """ Ensure tables are created  """
        df = pd.read_sql_query(self.q2, con=self.engine)
        assert len(df) == 3


if __name__ == '__main__':
    unittest.main()