#!/usr/bin/python3

import os

print("\u001b[38;2;180;180;255m========== metrolib ==========\u001b[0m")
os.system("cd metrolib && ninja")

print("\u001b[38;2;180;180;255m========== matcheroni ==========\u001b[0m")
os.system("cd matcheroni && ninja")

print("\u001b[38;2;180;180;255m========== metron ==========\u001b[0m")
os.system("cd metron && ./build.py && ninja")

print("\u001b[38;2;180;180;255m========== metroc ==========\u001b[0m")
os.system("cd metroc && ninja")

print("\u001b[38;2;180;180;255m========== metroboy ==========\u001b[0m")
os.system("cd metroboy && ninja")

print("\u001b[38;2;180;180;255m========== metronica ==========\u001b[0m")
os.system("cd metronica && ninja")



# gb_spu
# metroboy
# metronica
# picorvd
# pinwheel
# plait



# smhasher
# rv32iboy
# aappleby.github.io
# wideboard
