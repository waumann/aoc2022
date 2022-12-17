#!/usr/bin/python3

import re

with open("input.day15.txt", "r") as f:
  all = f.readlines()

def freq(x, y):
  return x * 4000000 + y

beacons = set()

bb = 0
for line in all:
  bb += 1
  print("Processing sensor %d" % bb)
  m = re.search('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
  sx = int(m.group(1))
  sy = int(m.group(2))
  bx = int(m.group(3))
  by = int(m.group(4))
  #print("S: (%d, %d), B: (%d, %d)" % (sx, sy, bx, by))
  dx = abs(sx - bx)
  dy = abs(sy - by)
  distance = dx + dy
  for y in range(sy - dy, sy + dy + 1):  
    if y < 0 or y > 4000000: continue
    dist_to_row = abs(sy - y)
    width = distance - dist_to_row
    for x in range(sx - width, sx + width + 1):
      if x < 0 or x > 4000000: continue
      beacons.add(freq(x, y))

print("Beacon :%s" % beacons)
