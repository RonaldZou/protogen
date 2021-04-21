#!/usr/bin/python
# -*- coding: utf-8 -*-
# module thread_worker
# Created by ronald on 2016/12/15.
"""
This module provides 

Static objects:

REQUIRED_MIN_VERSION -- Required min version number of the Python DLL.

Functions:

main() -- entrance function
"""

# import
import os
import sys
import traceback
from threading import Thread

try:
    import path_utils
    import sundry
    import thread_utils
except:
    print("import third part module error:", sys.exc_info()[0])
    raise

# Variables with simple values
REQUIRED_MIN_VERSION = "3.5"
MAIN_PARAM = None
CURRENT_DIR = os.path.dirname(path_utils.get_file_path(__file__))
LOG_FILE = "%s.log" % os.path.basename(os.path.realpath(__file__)).split(".")[0]


# class
class ThreadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.stop_all_threads = False

    def run(self):
        try:
            while True:
                if thread_utils.STOP_ALL_THREADS:
                    break
                # Get the work from the queue and expand the tuple
                # 从队列中获取任务并扩展tuple
                work_index, work_param = self.queue.get()
                self.work(work_index, work_param)
                self.queue.task_done()
        except Exception as e:
            self.stop_all_threads = True
            raise ''.join(traceback.format_exception(*sys.exc_info()))

    def work(self, work_index, work_param):
        pass
