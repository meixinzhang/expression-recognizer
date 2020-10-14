from src.common.logger import init_logger
import pandas as pd
import timeit

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class BaseHelpers(object):
    def __init__(self, name=None, name_log=None, log_level='INFO', config=None, **kwargs):

        """
            log_level is provided as input in order to be able to work with classes operating at
            different logging levels at the same time
        """

        log = kwargs.get('log' or None)
        # print(f'Log received: {log}')
        d = {
            10: 'DEBUG',
            20: 'INFO',
            30: 'WARNING',
            40: 'ERROR',
            50: 'CRITICAL'
        }
        log_level = d[log.getEffectiveLevel()] if log is not None else log_level
        self.name = name or __name__
        self.log_level = log_level if log is None else log.getEffectiveLevel()
        self.name_log = name_log if name_log is not None else str(self.__class__.__name__)
        self.pars = config if config is not None else dict()
        self.log = log.getChild(self.name_log) if log is not None else init_logger(self.name_log)
        self.log.setLevel(log_level.upper())
        self.debug = kwargs.get('debug', False)
        self._starttime = timeit.default_timer()

    def worktime(self):
        return timeit.default_timer() - self._starttime
