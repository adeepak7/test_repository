#!/usr/bin/env python3

import os
import sys
from subprocess import call


WORKING_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
ROOT = os.path.join(WORKING_DIR, '..')
TASKLIB = os.path.join(ROOT, 'src/')
INPUT_FILE_DIRECTORIES = os.path.join(ROOT, 'data/')
OUTPUT_FILE_DIRECTORIES = os.path.join(ROOT, 'results/')

command_line_call = "python " + TASKLIB + "test_module.py"\
                    + " -msg_from " + "Deepak"\
                    + " -inp_msg_file " + INPUT_FILE_DIRECTORIES + "message_from_deepak.txt"\
                    + " -o " + OUTPUT_FILE_DIRECTORIES + "output.txt"

call(command_line_call, shell=True)