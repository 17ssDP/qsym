#!/usr/bin/env python2
import atexit
import argparse
import logging
import functools
import hashlib
import json
import os
import pickle
import shutil
import subprocess as sp
import sys
import tempfile
import time

import pyinotify
import qsym


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("-o", dest="output", required=True,
                   help="Fuzzer output directory")
    p.add_argument("-a", dest="fuzzer", required=True, help="Fuzzer name")
    p.add_argument("-n", dest="name", required=True, help="Qsym name")
    p.add_argument("-f", dest="filename", default=None)
    p.add_argument("-m", dest="mail", default=None)
    p.add_argument("-b", dest="asan_bin", default=None)
    p.add_argument("-t", dest="timeout", default=120)
    p.add_argument(
        "cmd", nargs="+", help="cmdline, use %s to denote a file" % qsym.utils.AT_FILE)
    return p.parse_args()


def check_args(args):
    if not os.path.exists(args.output):
        raise ValueError('no such directory')

def mkdir(dirp):
    if not os.path.exists(dirp):
        os.makedirs(dirp)

def mk_dirs(output, fuzzer):
    fuzzer_output = output
    fuzzer_dir = os.path.join(fuzzer_output, fuzzer)
    fuzzer_queue = os.path.join(fuzzer_dir, "queue")
    fuzzer_state = os.path.join(fuzzer_queue, ".state")
    fuzzer_lenconfig = os.path.join(fuzzer_state, "lenconfig")
    fuzzer_target = os.path.join(fuzzer_state, "target")
    mkdir(fuzzer_output)
    mkdir(fuzzer_dir)
    mkdir(fuzzer_queue)
    mkdir(fuzzer_state)
    mkdir(fuzzer_lenconfig)
    mkdir(fuzzer_target)


def main():
    args = parse_args()
    mk_dirs(args.output, args.fuzzer)
    # check_args(args)
    
    server = qsym.server.SymServer(args.output, args.fuzzer)
    server.start()

    e = qsym.fuzzer.FuzzerExecutor(args.cmd, args.output, args.fuzzer,
                                   args.name, args.timeout, args.filename, args.mail, args.asan_bin)
    try:
        e.run()
    finally:
        e.cleanup()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
