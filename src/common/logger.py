import logging
import sys

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno == logging.WARNING:
            # record.msg = '\033[93m%s\033[0m' % record.msg
            record.levelname = '\033[93m%s\033[0m' % record.levelname
            record.name = '\033[93m%s\033[0m' % record.name
        elif record.levelno == logging.ERROR:
            # record.msg = '\033[91m%s\033[0m' % record.msg
            record.levelname = '\033[91m%s\033[0m' % record.levelname
            record.name = '\033[91m%s\033[0m' % record.name
        elif record.levelno == logging.INFO:
            record.levelname = '\033[36m%s\033[0m' % record.levelname
            record.name = '\033[36m%s\033[0m' % record.name
        return logging.Formatter.format(self, record)


def init_logger(name, log_level=logging.INFO, logfile=None, propagate=False, **kwargs):

    logger = logging.getLogger(name)
    log_format = "[%(levelname)s %(name)s] %(asctime)s - %(message)s"
    
    formatter = ColoredFormatter(log_format)
    ch = logging.StreamHandler(sys.stdout)

    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.propagate = propagate
    logger.setLevel(log_level)
    return logger