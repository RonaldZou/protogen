#!/usr/bin/python
# -*- coding: utf-8 -*-
# module file_utils
# from third-party
# Created by ronald on 2016/12/15.
"""
This module provides file methods

Static objects:

required_min_version -- Required min version number of the Python DLL.
CSHARP_EXTENSION -- CSharp file extension.
PROTO_EXTENSIONS -- Proto file extension.
XLSX_EXTENSION -- XLSX file extension.
CSV_EXTENSION -- CSV file extension.
META_EXTENSION -- meta file extension.

Functions:

get_file_name_without_extension(file_base_name) -- Get_file_name_without_extension.
get_file_extension(file_base_name) -- Get file extension.
change_file_extension(file_base_name, extension) -- Change file extension.
replace_text_in_file(replacements, file) -- Replace text in file
read_all(file_path) -- Read All text of file
backup(file_path) -- Backup file
"""
# import
import os
import time  # 引入time模块

# Variables with simple values
required_min_version = "3.5"
CSHARP_EXTENSION = ".cs"
CSPROJ_EXTENSION = ".csproj"
CSV_EXTENSION = ".csv"
META_EXTENSION = ".meta"
PNG_EXTENSION = ".png"
PROTO_EXTENSION = ".proto"
TXT_EXTENSION = ".txt"
XLSX_EXTENSION = ".xlsx"
ZIP_EXTENSION = ".zip"


# functions

def get_file_base_name(file_name):
    """
    Get base name of file
    :param file_name:
    :return:
    """
    return os.path.basename(file_name)


def get_file_name_without_extension(file_name):
    """
    Get_file_name_without_extension.
    :param file_name:
    :return:
    """
    return os.path.splitext(get_file_base_name(file_name))[0]


def get_file_extension(file_base_name):
    """
    Get file extension
    :param file_base_name:
    :return:
    """
    return os.path.splitext(file_base_name)[1]


def change_file_extension(file_base_name, extension):
    """
    Change file extension.
    :param file_base_name:
    :param extension:
    :return:
    """
    return "%s%s" % (get_file_name_without_extension(file_base_name), extension)


def replace_text_in_file(file, replacements):
    """
    Replace text in file
    :param file:
    :param replacements:
    :return:
    """
    in_file = open(file, 'r', encoding='utf-8')
    content = in_file.read()
    in_file.close()

    for (src, target) in replacements.items():
        content = content.replace(src, target)

    out_file = open(file, 'wb+')
    out_file.write(bytes(content, "utf8"))
    out_file.close()


def replace_text_in_file_with_fun(file, func):
    """
    Replace text in file
    :param file:
    :param func:
    :return:
    """
    if not func:
        return
    in_file = open(file, 'r', encoding='utf-8')
    content = in_file.read()
    in_file.close()
    content = func(content)
    out_file = open(file, 'wb+')
    out_file.write(bytes(content, "utf8"))
    out_file.close()


def insert(file, where, text, is_below=True):
    """
    Insert text to file
    :param file:
    :param where:
    :param text:
    :param is_below:
    :return:
    """
    in_file = open(file, 'r+', encoding='utf-8')
    content = in_file.read()
    in_file.close()
    if is_below is True:
        content = content.replace(where, "%s%s" % (text, where))
    else:
        content = content.replace(where, "%s%s" % (where, text))
    out_file = open(file, 'wb+')
    out_file.write(bytes(content, "utf8"))
    out_file.close()


def read_all(file_path):
    """
    Read All text of file
    :param file_path:
    :return:
    """
    file = open(file_path, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    return content


def backup(file_path):
    """
    Backup file
    :param file_path:
    :return:
    """

    if not os.path.isfile(file_path):
        return
    extension = get_file_extension(file_path)
    backup_file_path = file_path.replace(extension, "_%s%s" % (
        time.strftime("%Y-%m-%d-%H-%M-%s.backup", time.localtime()), extension))
    in_file = open(file_path, 'r+', encoding='utf-8')
    content = in_file.read()
    in_file.close()
    out_file = open(backup_file_path, 'wb+', encoding='utf-8')
    out_file.write(bytes(content))
    out_file.close()
