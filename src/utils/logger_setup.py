import logging
import os

# Ensure the log directory exists (create if missing)
log_dir = os.path.join(os.path.dirname(__file__), '..', 'bins', 'logs')
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, 'app.log')

# Create logger instance
logger = logging.getLogger("cllama")
logger.setLevel(logging.DEBUG)

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# File handler
fh = logging.FileHandler(log_file)
fh.setLevel(logging.DEBUG)

# Formatter with filename and function name
formatter = logging.Formatter(
    '(%(name)s) [%(levelname)s] [%(asctime)s] [%(filename)s:%(funcName)s] %(message)s'
)

# Set formatter for both handlers
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)
