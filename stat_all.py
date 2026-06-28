#!/usr/bin/python3

import os
import glob
import subprocess

def run(tag, cmd):
    print(tag, end="")
    ret = subprocess.check_output(cmd, shell=True)
    print(ret.decode(), end="")

run("\u001b[38;2;180;255;180mMETAREPO __________________________ \u001b[0m",
    "git -c color.status=always status -s -b")

for dir in sorted(glob.glob("*")):
    if not os.path.exists(dir + "/.git"): continue
    run(f"\u001b[38;2;180;180;255m{(dir + ' ').ljust(35, '_')} \u001b[0m",
                f"cd {dir} && git -c color.status=always status -s -b")

print("Broken symlinks: ")
os.system("find . -xtype l")

