"""DataLog module"""

import logging

__author__ = "Sean Leavey <datalog@attackllama.com>/small changes by cmo <software@contextuallight.com>"
__version__ = "0.7.9"

# suppress warnings when the user code does not include a handler
logging.getLogger().addHandler(logging.NullHandler())
