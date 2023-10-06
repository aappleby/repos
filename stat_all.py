#!/usr/bin/python3

#import glob
#for x in glob.iglob('*'):
#    print(x)

import os

#printf("\u001b[38;2;255;255;255m", (color >> 0) & 0xFF, (color >> 8) & 0xFF, (color >> 16) & 0xFF);
#printf("\u001b[0m");


root_dir = os.getcwd();

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


print(f"\u001b[38;2;180;180;255m========== METAREPO ==========\u001b[0m")
os.system(f"git status -s")
os.system(f"git log --branches --not --remotes")
