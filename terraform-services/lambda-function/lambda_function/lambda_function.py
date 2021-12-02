#!/usr/bin/env python3

"""
TBC
"""

# Native Imports

import sys
import logging

# Third Party Imports


LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdut))


def lambda_handler(event, context):
    """

    Args:
        event ([type]): [description]
        context ([type]): [description]
    """

    LOGGER.info('Recieved Event: %s', event)
