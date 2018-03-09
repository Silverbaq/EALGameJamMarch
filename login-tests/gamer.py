#!/bin/python

import logging
import os

logger = logging.getLogger('gamer_application')
fh = logging.FileHandler('/tmp/temp.log')
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

print("You have connected as gamer !!")

pid = os.getpid()
logger.info("hi from gamer {}".format(pid))
print("continue to be awesome... bye")
