#!/usr/bin/python3

import os

with open("input.day7.txt", "r") as f:
  all = f.readlines()

hier = dict()
path_dict = hier
hier["DATA"] = 0
cwd = []
sizes = []

def get_size_with_subdirs(path_dict):
  global sizes
  size = path_dict["DATA"]
  for k in path_dict.keys():
    if k != "DATA":
      subdir_dict = path_dict[k]
      size += get_size_with_subdirs(subdir_dict)
  sizes.append(size)
  return size

for line in all:
  l = line.strip()
  print("Got: '%s'" % l)
  if l.startswith("$ cd"):
    path = l[5:]
    if path == "/":
      cwd = []
      path_dict = hier
    elif path == "..":
      cwd.pop()
      path_dict = hier
      for c in cwd:
        path_dict = path_dict[c]
    else:
      cwd.append(path)
      path_dict = path_dict[path]
    pp = os.path.join("/", *cwd)
    print ("cwd is %s" % pp)
  elif l.startswith("$ ls"):
    pass
  elif l.startswith("dir"):
    path_dict.setdefault(l[4:], {})
    path_dict[l[4:]].setdefault("DATA", 0) 
  else:
    (size, _) = l.split(" ")
    path_dict["DATA"] += int(size)

root_size = get_size_with_subdirs(hier)
print("Total used = %d" % root_size)
target_size = root_size - 40000000
print("Need to free up %d" % target_size)
sorted_sizes = sorted(sizes)
val = 0
for s in sorted_sizes:
  if s >= target_size:
    print("Smallest dir to clear = %d" % s)
    break
