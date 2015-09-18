#! /usr/bin/python3

import sys

total = len(sys.argv)
for a in sys.argv[1:]:
    print("The script name is args.py")
    print("Got %d command-line arguments" % (total))
    print("Here they are:")
    print(a)
