from logging import Formatter, getLogger, INFO
from logging.handlers import RotatingFileHandler


logger = getLogger('civ-hooks-matrix')
logger.setLevel(INFO)
handler = RotatingFileHandler('./var/log/hooks.log', maxBytes=1024*1024, backupCount=5)
handler.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)


__all__ = ['logger']