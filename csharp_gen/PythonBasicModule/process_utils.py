#!/usr/bin/python
# -*- coding: utf-8 -*-
# module process_utils
# from third-party
#  Created by ronald on 2016/12/15.
"""
This module provides file methods

Static objects:

required_min_version -- Required min version number of the Python DLL

Functions:

run(command) -- Run command with arguments.
"""
# import
import logging
import os
import shlex
import subprocess

# Variables with simple values
required_min_version = "3.5"


# functions
def run(command):
    """
    Run command with arguments.
    :param command:
    :return:
    """
    logging.debug(command)
    return os.system(command)


def run_sub_process(command):
    """
    Run command with arguments in sub process.
    :param command:
    :return:
    """
    logging.debug(command)
    args = shlex.split(command, comments=False, posix=False)
    return subprocess.run(args, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=True)


