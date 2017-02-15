import logging
import sys

root = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s -  %(message)s')


def set_root_level(logging_level):
    root.setLevel(logging_level)


def add_sysout_handler(logging_level):
    # System out handler
    sysouth = logging.StreamHandler(sys.stdout)
    sysouth.setLevel(logging_level)
    sysouth.setFormatter(formatter)
    root.addHandler(sysouth)


def add_file_handler(logging_level, filename):
    # File Handler
    fileh = logging.FileHandler(filename)
    fileh.setLevel(logging_level)
    fileh.setFormatter(formatter)
    root.addHandler(fileh)


def get_logger(name):
    return logging.getLogger(name)
