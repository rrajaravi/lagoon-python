import os
import re

__author__ = "Raja Ravi"
__license__ = "MIT"
__credits__ = ["Raja Ravi, Sathya Narrayanan"]
__version__ = "1.0.0"
__maintainer__ = "Raja Ravi"
__email__ = "r.rajaravi@gmail.com"

def connect(
    host: str=None,
    port: int=None,
    version="v1.0"
) -> "LagoonClient":
    """
    Returns a Client object
    :param host: hostname of lagoon server
    :param port: port of lagoon service
    """
    from lagoon.client import LagoonClient
    
    return LagoonClient(
        host,
        port
    )