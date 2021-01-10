import tkinter as tk
from tkinter import *

import logging


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level='DEBUG',
    filename='grocery_billing_software_logs.txt'
)

logger = logging.getLogger('test_logger')

