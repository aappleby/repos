#!/usr/bin/python3

import os
import sys
import subprocess

def run(tag, cmd):
	print(tag, end="");
	sys.stdout.flush()
	ret = subprocess.check_output(cmd, shell=True)
	print(ret.decode(), end="")


run(f"\u001b[38;2;180;255;180mMETAREPO __________________________ \u001b[0m",
    f"git -c color.status=always status -s -b")

for root, dirs, files in os.walk('.'):
	#for dir in sorted(dirs):
    if root == ".":
        continue
    if not os.path.exists(root + "/.git"):
        continue
    #print(root)
    run(f"\u001b[38;2;180;180;255m{(root + ' ').ljust(50, '_')} \u001b[0m",
                f"cd {root} && git -c color.status=always status -s -b")
	#break

print()
print("Broken symlinks: ")
os.system("find . -xtype l")
print()
