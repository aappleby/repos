#!/usr/bin/python3

import os

def run(command):
	result = os.system(command)
	if result != 0:
		print(f"\u001b[38;2;255;180;180m========== Command '{command}' failed ==========\u001b[0m")
		quit(-1)

print("\u001b[38;2;180;180;255m========== metrolib ==========\u001b[0m")
run("cd metrolib && ninja -t clean")

print("\u001b[38;2;180;180;255m========== matcheroni ==========\u001b[0m")
run("cd matcheroni && ninja -t clean")
run("cd matcheroni && ninja -f build_docs.ninja -t clean")

print("\u001b[38;2;180;180;255m========== metron ==========\u001b[0m")
run("cd metron && ./build.py && ninja -t clean")

print("\u001b[38;2;180;180;255m========== metroc ==========\u001b[0m")
run("cd metroc && ninja -t clean")

print("\u001b[38;2;180;180;255m========== metroboy ==========\u001b[0m")
run("cd metroboy && ninja -t clean")

print("\u001b[38;2;180;180;255m========== metronica ==========\u001b[0m")
run("cd metronica && ninja -t clean")

#print("\u001b[38;2;180;180;255m========== picorvd ==========\u001b[0m")
#run("cd picorvd && ./build.sh")

# pinwheel
# plait

# smhasher
# rv32iboy
# aappleby.github.io
# wideboard

print("\u001b[38;2;180;255;180m========== Clean OK ==========\u001b[0m")
