#!/usr/bin/python
# -*- coding: utf-8 -*-
# module path_utils
# from third-party
# Created by ronald on 2016/12/15.
"""
This module provides file methods

Static objects:

required_min_version -- Required min version number of the Python DLL

Functions:

get_current_dir() -- Get the direction of caller's python file.
touch_direction(dir_name) -- Make direction if it is not exist.
rm(dir_or_file) -- rm -rf
make_relative_path(p1, p2, sep, pardir) -- Determines the difference between two path.
walk_with_ignore(dir_name, extensions, ignored_folders, ignored_files) -- Directory tree generator with ignore.
get_empty_folders(dir_name) -- Get all empty folders.
"""
# import
import logging
import os
import shutil
import sys
try:
    sys.path.append(os.path.join(os.path.dirname(__file__)))
    import array_utils
    import file_utils
    import path_utils
except ImportError:
    print('We need basic self module, sorry...')
    sys.exit(-1)

# Variables with simple values
required_min_version = "3.5"


# functions
def get_file_path(file):
    """
    get the path of file.
    :return:
    """
    return os.path.dirname(os.path.realpath(file))


def get_absolute_path(dir_name):
    """
    Get absolute path.
    :param dir_name:
    :return:
    """
    if os.path.isabs(dir_name):
        return dir_name
    else:
        return os.path.abspath(dir_name)


def get_relative_path(dir_name):
    """
    Get relative path.
    :param dir_name:
    :return:
    """
    if os.path.isabs(dir_name):
        return os.path.relpath(dir_name)
    else:
        return dir_name


def touch_dir(dir_name):
    """
    Make direction if it is not exist.
    :param dir_name:
    :return:
    """
    if not os.path.exists(dir_name):
        mk_dir(dir_name)


def mk_dir(dir_name):
    """
    make direction
    :param dir_name:
    :return:
    """
    dir_name = dir_name.strip()
    dir_name = dir_name.rstrip("\\")

    if not os.path.exists(dir_name):
        logging.debug(dir_name + ' 创建成功')
        os.makedirs(dir_name)
        return True
    else:
        logging.debug(dir_name + ' 目录已存在')
        return False


def rm(dir_or_file):
    """
    rm -rf
    :param dir_or_file:
    :return:
    """
    if os.path.exists(dir_or_file):
        if os.path.isfile(dir_or_file):
            os.remove(dir_or_file)
        else:
            shutil.rmtree(dir_or_file)


def make_relative_path(p1, p2, sep=os.path.sep, pardir=os.path.pardir):
    """
    Determines the difference between two path.
    :param p1:
    :param p2:
    :param sep:
    :param pardir:
    :return:
    """
    same, (u1, u2) = array_utils.diff_arrays(p1.split(sep), p2.split(sep))
    if not same:
        return p2
    return sep.join([pardir] * len(u1) + u2)


def walk_with_ignore(dirs_name, extensions=[], ignored_folders=[], ignored_files=[], file_names=[]):
    """
    Directory tree generator with ignore.
    :param dirs_name:
    :param extensions:
    :param ignored_folders:
    :param ignored_files:
    :param file_names:
    :return:
    """
    selected_files = []
    for dir_name in dirs_name:
        for root, dirs, files in os.walk(dir_name):
            is_ignored = False
            for ignored_folder in ignored_folders:
                if make_relative_path(dir_name, root).startswith(os.path.normpath(ignored_folder)):
                    is_ignored = True
                    break
            if is_ignored is True:
                continue
            for file in files:
                if len(file_names) > 0 and not (file_utils.get_file_base_name(file) in file_names):
                    continue
                if file in ignored_files:
                    continue
                if len(extensions) > 0 and not (file_utils.get_file_extension(file) in extensions):
                    continue
                selected_files.append(os.path.join(root, file))
    return selected_files


def walk_dirs_with_ignore(dirs_name, ignored_folders=[]):
    """
    Directory tree generator with ignore.
    :param dirs_name:
    :param ignored_folders:
    :return:
    """
    selected_dirs = []
    for dir_name in dirs_name:
        for root, dirs, files in os.walk(dir_name):
            if os.path.basename(root) in ignored_folders:
                break
            for found_dir in dirs:
                if os.path.basename(found_dir) in ignored_folders:
                    continue
                selected_dirs.append(os.path.join(root, found_dir))
    return selected_dirs


def get_empty_folders(dir_name, ignored_folders=[]):
    """
    Get all empty folders.
    :param dir_name:
    :param ignored_folders:
    :return:
    """
    selected_folders = []
    for root, dirs, files in os.walk(dir_name):
        is_ignored = False
        for ignored_folder in ignored_folders:
            if str.find(root, ignored_folder) >= 0:
                is_ignored = True
                break
        if is_ignored is True:
            continue
        for folder in dirs:
            folder = os.path.join(root, folder)
            if not os.listdir(folder):
                selected_folders.append(path_utils.make_relative_path(dir_name, folder))
    return selected_folders

