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
    r_hist.append(r)
    r += int(ln.split(" ")[1])

for i in [20, 60, 100, 140, 180, 220]:
  strength += i * r_hist[i]

print(strength)
