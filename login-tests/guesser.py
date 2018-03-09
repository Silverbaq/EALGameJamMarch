#!/usr/bin/env python

import logging
import os
import time

logger = logging.getLogger('gamer_application')
fh = logging.FileHandler('/tmp/temp.log')
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

print("You have connected as guesser !!")

while True:
    pid = os.getpid()
    logger.info("hi from guesser {}".format(pid))
    time.sleep(5)

print("continue to be awesome... bye")
