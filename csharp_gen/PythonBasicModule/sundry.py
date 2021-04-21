#!/usr/bin/python
# -*- coding: utf-8 -*-
# module sundry
# from third-party
# by generator ronald
# Created by ronald on 2016/12/15.
"""
This module provides file methods

Static objects:

required_min_version -- Required min version number of the Python DLL

Functions:

is_number(value) -- Check is number.
init_logging(log_filename) --- init logging.
check_python_version(version) --- check python version.
check_python_max_version(version) --- check python version.

"""
# import
import sys
import logging

# Variables with simple values
required_min_version = "3.5"


# functions
def is_number(value):
    """
    Check is number.
    :param value:
    :return:
    """
    try:
        int(value)
    except TypeError:
        return False
    except ValueError:
        return False
    except Exception as error:
        logging.exception(error)
        return False
    else:
        return True


def init_logging(log_filename):
    """
    init logging.
    :param log_filename:
    :return:
    """
    # 配置日志信息
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=log_filename,
                        filemode='w')
    # 定义一个Handler打印INFO及以上级别的日志到sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # 设置日志打印格式
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    # 将定义好的console日志handler添加到root logger
    logging.getLogger('').addHandler(console)


def check_python_version(version):
    """
    check python version.
    :param version:
    :return:
    """
    version_array = str.split(version, ".")
    current_version = sys.version_info
    if current_version[0] == int(version_array[0]) and current_version[1] >= int(version_array[1]):
        pass
    else:
        logging.warning("[%s] - Error: Your Python interpreter is %d.%d , "
                        "while it must be %s.%s or greater (within major version %s)\n" %
                        (sys.argv[0], current_version[0], current_version[1], version_array[0], version_array[1], version_array[0]))
        sys.exit(-1)
    return 0


def check_python_max_version(version):
    """
    check python version.
    :param version:
    :return:
    """
    version_array = str.split(version, ".")
    current_version = sys.version_info
    if current_version[0] == int(version_array[0]) and current_version[1] <= int(version_array[1]):
        pass
    else:
        logging.warning("[%s] - Error: Your Python interpreter is %d.%d , "
                        "while it must be %s.%s or litter (within major version %s)\n" %
                        (sys.argv[0], current_version[0], current_version[1], version_array[0], version_array[1], version_array[0]))
        sys.exit(-1)
    return 0
