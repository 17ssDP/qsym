#!/usr/bin/env python2
import argparse
import logging
from qsym import Executor, utils

l = logging.getLogger('run_qsym')

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("-i", dest="input_file", help="An input file", required=True)
    p.add_argument("-o", dest="output_dir", help="An output directory", required=True)
    p.add_argument("-b", dest="bitmap", help="A bitmap file")
    p.add_argument("cmd", nargs="+",
            help="Command to execute: use %s to denote a file" % utils.AT_FILE)
    p.add_argument("-j", dest="target_list", help="A target list file")
    return p.parse_args()

def main():
    args = parse_args()
    q = Executor(args.cmd,
            args.input_file,
            args.output_dir,
            args.bitmap,
            args.target_list)
    q.run(120)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
