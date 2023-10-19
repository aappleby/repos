#!/usr/bin/python3

import os
import sys
import subprocess

def run(tag, cmd):
	print(tag, end="");
	sys.stdout.flush()
	subprocess.run(cmd, shell=True)
	#print(ret.decode(), end="")

for root, dirs, files in os.walk('.'):
	for dir in sorted(dirs):
		if dir.startswith("."):
			continue
		if not os.path.exists(dir + "/.git"):
			continue
		run(f"\u001b[38;2;180;180;255m{(dir + ' ').ljust(35, '=')} \u001b[0m",
                    f"cd {dir} && git checkout main")
		run(f"\u001b[38;2;180;180;255m{(dir + ' ').ljust(35, '=')} \u001b[0m",
                    f"cd {dir} && git checkout master")
	break


