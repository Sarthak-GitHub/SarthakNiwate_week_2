# Python Module example
import logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
logger.setLevel(logging.INFO)

def sub(a, b):
    """This program subtracts two
    numbers and return the result"""
    result = a - b
    return result
