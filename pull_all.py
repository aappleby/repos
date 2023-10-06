#!/usr/bin/python3

import os

print(f"\u001b[38;2;180;255;180m========== METAREPO ==========\u001b[0m")
os.system(f"git pull")

for root, dirs, files in os.walk('.'):
	for dir in sorted(dirs):
		if dir.startswith("."):
			continue
		if not os.path.exists(dir + "/.git"):
			continue
		print(f"\u001b[38;2;180;180;255m========== {dir} ==========\u001b[0m")
		os.system(f"cd {dir} && git pull")
	break


