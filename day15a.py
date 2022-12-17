#!/usr/bin/python3

import sys
import re

with open("input.day15.txt", "r") as f:
  all = f.readlines()

row = int(sys.argv[1])
print("Row = %d" % row)

beacons = set()
no_beacons = set()

for line in all:
  m = re.search('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
  sx = int(m.group(1))
  sy = int(m.group(2))
  bx = int(m.group(3))
  by = int(m.group(4))
  #print("S: (%d, %d), B: (%d, %d)" % (sx, sy, bx, by))
  if row == by:
    beacons.add(bx) 
  assert(sy != row)
  dx = abs(sx - bx)
  dy = abs(sy - by)
  distance = dx + dy
  if sy < row and sy + distance < row:
    continue
  if sy > row and sy - distance > row: continue
  dist_to_row = abs(row - sy)
  width = distance - dist_to_row
  for x in range(sx - width, sx + width + 1):
    no_beacons.add(x)

intersection = no_beacons.difference(beacons)
print("Points without beacons: %d" % len(intersection))
#print("Beacons: %s" % beacons)
#print("No Beacons: %s" % no_beacons)
#print("Intersection: %s" % intersection)
