#!/usr/bin/env python

import logging
from degate.spot import Spot as Client
from degate.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

AccountAddress = "0xba2b5feae299808b119fd410370d388b2fbf744b"
AssetPrivateKey = ""
AccountId = 7

client = Client(AccountAddress,AssetPrivateKey,AccountId)

try:
    logging.info(client.account())
except Exception as e:
    logging.error(e)


