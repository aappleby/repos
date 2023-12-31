#!/usr/bin/python3

import os

def run(command):
	result = os.system(command)
	if result != 0:
		print(f"\u001b[38;2;255;180;180m========== Command '{command}' failed ==========\u001b[0m")
		quit(-1)

print("\u001b[38;2;180;180;255m========== metrolib ==========\u001b[0m")
run("cd metrolib && ninja")

print("\u001b[38;2;180;180;255m========== matcheroni ==========\u001b[0m")
run("cd matcheroni && ninja")
run("cd matcheroni && ninja -f build_docs.ninja")

print("\u001b[38;2;180;180;255m========== metron ==========\u001b[0m")
run("cd metron && ./build.py && ninja")

print("\u001b[38;2;180;180;255m========== metroc ==========\u001b[0m")
run("cd metroc && ninja")

print("\u001b[38;2;180;180;255m========== metroboy ==========\u001b[0m")
run("cd metroboy && ninja")

print("\u001b[38;2;180;180;255m========== metronica ==========\u001b[0m")
run("cd metronica && ninja")

print("\u001b[38;2;180;180;255m========== picorvd ==========\u001b[0m")
run("cd picorvd && ./build.sh")

print("\u001b[38;2;180;180;255m========== plait ==========\u001b[0m")
run("cd plait && ninja")

print("\u001b[38;2;180;180;255m========== wideboard ==========\u001b[0m")
run("cd wideboard && tsc -v")

print("\u001b[38;2;180;180;255m========== pinwheel ==========\u001b[0m")
run("cd pinwheel && ninja")

# smhasher
# rv32iboy
# aappleby.github.io

print("\u001b[38;2;180;255;180m========== Build OK ==========\u001b[0m")
