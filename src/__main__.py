#! /usr/bin/env python3

import sys

if __name__ == "__main__":
    pyv = sys.version.split()[0]

    if sys.version_info < (3, 7):
        print("ppy requires python 3.7, you are using %s" % (pyv))
        sys.exit(1)

    import ppy
    ppy.main()
