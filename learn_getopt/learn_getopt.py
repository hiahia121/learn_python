# -*- encoding: utf-8 -*-

import sys
import getopt


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "file="])
    for item in opts:
        print item
