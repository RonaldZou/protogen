#!/usr/bin/python
# -*- coding: utf-8 -*-
# module array_utils
# from third-party
# Created by ronald on 2016/12/15.
"""
This module provides array methods

Static objects:

required_min_version -- Required min version number of the Python DLL

Functions:

is_all_values_same(array) -- Check is all values of array is the same.
diff_arrays(*sequences) -- Get the different parts of arrays.
"""
# no import

# Variables with simple values

required_min_version = "3.5"


# functions
def is_all_values_same(array):
    """
    Check is all values of array is the same.
    :param array:
    :return:
    """
    if len(array) <= 1:
        return True
    first_value = array[0]
    for other_value in array[1:]:
        if other_value != first_value:
            return False
    return True


def diff_arrays(*arrays):
    """
    Get the different parts of arrays.
    :param arrays:
    :return:
    """
    if not arrays:
        return [], []
    same = []
    for values in zip(*arrays):
        if not is_all_values_same(values):
            break
        same.append(values[0])
    return same, [array[len(same):] for array in arrays]

