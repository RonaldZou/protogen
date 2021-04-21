#!/usr/bin/python
# -*- coding: utf-8 -*-
# module GenerateClientProto
# from third-party
# by generator ronald
"""
This script generate client csharp files from server protos.

Functions:
main -- Main process.

"""
# import
import json
import logging
import os
import re
import shutil
import sys

try:
    sys.path.append("../../PythonBasicModule")
    import file_utils
    import path_utils
    import process_utils
    import sundry
    import thread_utils
    import thread_worker
except:
    print("import third part module error:", sys.exc_info()[0])
    raise

# Variables with simple values
required_min_version = "3.5"
MAIN_PARAM = None
LOG_FILE = "%s.log" % os.path.basename(os.path.realpath(__file__)).split(".")[0]
IGNORE_PROTO_FOLDERS = ["google"]
IGNORE_PROTO_FILES = []


# class
class CommandLineParam:
    def __init__(self, argv):
        if len(argv) == 4:
            self.msg_dir = os.path.realpath(argv[1])
            self.client_proto_dir = os.path.realpath(argv[2])
            self.tool_proto_dir = os.path.realpath(argv[3])
            self.protoc_exe = os.path.join(self.tool_proto_dir, "protoc.exe")
            self.proto_files_dirs = [self.msg_dir]
            self.setting_file = "%s/setting.json" % self.msg_dir
            self.setting = json.loads(file_utils.read_all(self.setting_file))
        else:
            logging.error(
                "Invalid params:\n1 -- dir of server\n2 -- dir of client protobuf\n3 -- dir of tool protobuf\n")
            sys.exit(-1)


class Proto2CSharpWorker(thread_worker.ThreadWorker):
    def work(self, work_index, work_param):
        [proto_files] = work_param
        proto_file = proto_files[work_index]
        process_utils.run("%s -I=%s --csharp_out=%s %s" % (MAIN_PARAM.protoc_exe,
                                                           MAIN_PARAM.msg_dir,
                                                           MAIN_PARAM.client_proto_dir,
                                                           proto_file))


def csharp_file_replace(file_content):
    found = re.findall(r': pb::IMessage<(.+)>', file_content)
    for i in found:
        if MAIN_PARAM.setting['AllCsharpFileIgnore']:
            continue
        if i in MAIN_PARAM.setting['CsharpFileIgnore']:
            continue
        interface_class_name = ''
        if i.startswith('SC'):
            interface_class_name = 'TapPlot.ISCMessage'
            if MAIN_PARAM.setting['AllSCCsharpFileIgnore']:
                continue
        if i.startswith('CS'):
            interface_class_name = 'TapPlot.ICSMessage'
            if MAIN_PARAM.setting['AllCSCsharpFileIgnore']:
                continue
        if len(interface_class_name) > 0:
            file_content = file_content.replace(": pb::IMessage<%s>" % i,
                                                ": %s, pb::IMessage<%s>" % (interface_class_name, i))
    return file_content


# functions
def main():
    """
    main
    :return:
    """
    # generate csharp files from proto files
    for file in path_utils.walk_with_ignore([MAIN_PARAM.client_proto_dir], [file_utils.CSHARP_EXTENSION], []):
        path_utils.rm(file)
    proto_files = path_utils.walk_with_ignore(MAIN_PARAM.proto_files_dirs, extensions=[file_utils.PROTO_EXTENSION],
                                              ignored_folders=IGNORE_PROTO_FOLDERS, ignored_files=IGNORE_PROTO_FILES)
    thread_utils.work_with_thread(Proto2CSharpWorker, len(proto_files), [proto_files])
    # replace contents of csharp files
    for file in path_utils.walk_with_ignore([MAIN_PARAM.client_proto_dir], [file_utils.CSHARP_EXTENSION], []):
        file_utils.replace_text_in_file_with_fun(file, csharp_file_replace)
    return 0


if "__main__" == __name__:
    sundry.init_logging(LOG_FILE)
    sundry.check_python_version(required_min_version)
    MAIN_PARAM = CommandLineParam(sys.argv)
    sys.exit(main())
