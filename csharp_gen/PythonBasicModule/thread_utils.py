#!/usr/bin/python
# -*- coding: utf-8 -*-
# module thread_utils
# Created by ronald on 2016/12/15.
"""
This module provides 

Static objects:

REQUIRED_MIN_VERSION -- Required min version number of the Python DLL.

Functions:

work_with_thread(worker, work_count, work_param) -- work with queue
lock() -- lock thread
unlock -- unlock thread
"""

# import
import os
from queue import Queue
import threading
import traceback
import sys

try:
    import path_utils
    import sundry
except:
    print("import third part module error:", sys.exc_info()[0])
    raise

# Variables with simple values
REQUIRED_MIN_VERSION = "3.5"
CURRENT_DIR = os.path.dirname(path_utils.get_file_path(__file__))
LOG_FILE = "%s.log" % os.path.basename(os.path.realpath(__file__)).split(".")[0]
CPU_COUNT = os.cpu_count()
WORKER_MUTEX = threading.Lock()
STOP_ALL_THREADS = False


# class


# functions
def work_with_thread(worker_maker, work_count, work_param):
    """
    work with queue
    :param worker_maker:
    :param work_count:
    :param work_param:
    :return:
    """
    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 8 worker threads
    # 创建八个工作线程
    for x in range(CPU_COUNT):
        worker = worker_maker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        # 将daemon设置为True将会使主线程退出，即使worker都阻塞了
        worker.daemon = True
        try:
            worker.start()
        except Exception as e:
            worker.stop_all_threads = True
            raise ''.join(traceback.format_exception(*sys.exc_info()))
        # Put the tasks into the queue as a tuple
        # 将任务以tuple的形式放入队列中
    for i in range(work_count):
        queue.put((i, work_param))
        # Causes the main thread to wait for the queue to finish processing all the tasks
        # 让主线程等待队列完成所有的任务
    queue.join()


def lock():
    """
    lock thread
    :return:
    """
    WORKER_MUTEX.acquire()


def unlock():
    """
    unlock thread
    :return:
    """
    WORKER_MUTEX.release()
