#!/usr/bin/python3

import os
import glob
import subprocess

# Claude.ai wrote this, seems to work
def staleness(path, do_fetch=True):
    def git(*args):
        return subprocess.run(["git", "-C", path, *args],
                              capture_output=True, text=True).stdout.strip()
    if do_fetch:
        git("fetch", "-q", "origin")
    # resolve upstream default branch (origin/HEAD), with fallbacks
    up = git("rev-parse", "--abbrev-ref", "origin/HEAD")
    if not up or up.endswith("HEAD"):
        up = next((c for c in ("origin/main", "origin/master")
                   if git("rev-parse", "--verify", "-q", c)), "")
    if not up:
        return "no upstream"
    counts = git("rev-list", "--left-right", "--count", f"HEAD...{up}")
    if not counts:
        return "?"
    ahead, behind = (int(x) for x in counts.split())
    if not ahead and not behind:
        return f"up to date  ({up})"
    bits = []
    if behind: bits.append(f"{behind} behind")
    if ahead:  bits.append(f"{ahead} ahead")
    return f"{', '.join(bits)}  ({up})"


tag_meta = 'METAREPO '.ljust(52, '_') + " "
cmd_meta = "git status -s -b"
print(tag_meta, end="")
print(staleness(".", True).ljust(30, ' '), end="")
ret = subprocess.check_output(cmd_meta, shell=True).decode().strip()
print(ret)

my_repos = []
tp_repos = []

for dirpath, dirnames, filenames in os.walk("."):
    if dirpath == "." or not os.path.exists(dirpath + "/.git"):
        continue
    if dirpath.count('/') > 2:
        continue
    dirpath = dirpath[2:]
    if "third_party" in dirpath:
        tp_repos.append(dirpath)
    else:
        my_repos.append(dirpath)

for dirpath in my_repos:
    tag1 = f"{(dirpath + ' ').ljust(52, '_')} "
    cmd1 = f"cd {dirpath} && git status -s -b"

    print(tag1, end="")
    print(staleness(dirpath, True).ljust(30, ' '), end="")
    ret = subprocess.check_output(cmd1, shell=True).decode().strip()
    print(ret)

print("---------")

for dirpath in tp_repos:
    tag1 = f"{(dirpath + ' ').ljust(52, '_')} "
    cmd1 = f"cd {dirpath} && git status -s -b"

    print(tag1, end="")
    print(staleness(dirpath, True).ljust(30, ' '), end="")
    ret = subprocess.check_output(cmd1, shell=True).decode().strip()
    print(ret)

print("Broken symlinks: ")
os.system("find . -xtype l")

