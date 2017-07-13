# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logHdlr_File = logging.FileHandler('opsk_api_test.log', 'w')
logHdlr_File.setFormatter(logging.Formatter('%(asctime)s %(name)-4s %(levelname)-4s %(message)s'))
logger.addHandler(logHdlr_File)

