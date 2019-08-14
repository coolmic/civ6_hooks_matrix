from logging import Formatter, getLogger
from logging.handlers import RotatingFileHandler


def init_flask_loggers(app):
    # configure werkzeug logger
    werkzeug_handler = RotatingFileHandler('./var/log/werkzeug.log', maxBytes=1024*1024, backupCount=9)
    werkzeug_handler.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    getLogger('werkzeug').addHandler(werkzeug_handler)


__all__ = ['init_flask_loggers']