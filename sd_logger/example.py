#!/usr/bin/env python

import logging
import sd_logger

sd_logger.set_root_level(logging.DEBUG)
sd_logger.add_sysout_handler(logging.DEBUG)
sd_logger.add_file_handler(logging.ERROR, "test.log")
m_log = sd_logger.get_logger("test")

m_log.info("Test the sdlogger module !")

m_log.error("Oh, Error in example.py!")
