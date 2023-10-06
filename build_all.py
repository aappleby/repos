#!/usr/bin/python3

import os
import glob

root_dir = os.getcwd();
print(os.getcwd())

# metrolib
print("building metrolib")
os.system("cd metrolib && ninja")

# matcheroni
print("building matcheroni")
os.system("cd matcheroni && ninja")

# metron
print("building metron")
os.system("cd metron && ./build.py && ninja")


# aappleby.github.io
# gb_spu
# metroboy
# metroc
# metronica
# picorvd
# pinwheel
# plait
# rv32iboy
# smhasher
# wideboard
