#!/usr/bin/python3

import os

with open("input.day10.txt", "r") as f:
  all = f.readlines()

t = 1
r = 1
r_hist = [1]
strength = 0

for l in all:
  ln = l.strip()
  r_hist.append(r)
  if ln != "noop":
    print("DEBUG: %s" % ln)
    r_hist.append(r)
    r += int(ln.split(" ")[1])

msg = ""
for y in range(0, 6):
  for x in range(0, 40):
    t = x + y * 40 + 1
    if abs(x - r_hist[t]) <= 1:
      msg += "#"
    else:
      msg += " "
  print(msg)
  msg = ""
