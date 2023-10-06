#!/usr/bin/python3

import os

print(f"\u001b[38;2;180;255;180m========== METAREPO ==========\u001b[0m")
os.system(f"git status -s")
os.system(f"git log --branches --not --remotes")
os.system("find . -xtype l")

for root, dirs, files in os.walk('.'):
	for dir in sorted(dirs):
		if dir.startswith("."):
			continue
		if not os.path.exists(dir + "/.git"):
			continue
		print(f"\u001b[38;2;180;180;255m========== {dir} ==========\u001b[0m")
		os.system(f"cd {dir} && git status -s")
		os.system(f"cd {dir} && git log --branches --not --remotes")
	break


