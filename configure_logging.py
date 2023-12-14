# logging_config.py

import logging
from logging import getLogger
from logging.handlers import RotatingFileHandler


def configure_logging():
    # Configure the root logger
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

    # Configure the Waitress logger
    logger = getLogger("waitress")
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set the log level
    handler = RotatingFileHandler(
        "waitress.log", maxBytes=10000000, backupCount=5)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set the formatter for the handler
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
