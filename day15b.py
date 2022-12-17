#!/usr/bin/python3

import re

with open("input.day15.txt", "r") as f:
  all = f.readlines()

def freq(x, y):
  return x * 4000000 + y

def mergeIntervals(intervals):
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
        # Check for overlapping interval,
        # if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
 
    return stack

sx = []
sy = []
bx = []
by = []
dx = []
dy = []
distance = []
i = 0
for line in all:
  print("Processing sensor %d" % i)
  m = re.search('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
  sx.append(int(m.group(1)))
  sy.append(int(m.group(2)))
  bx = int(m.group(3))
  by = int(m.group(4))
  tdx = abs(sx[i] - bx)
  tdy = abs(sy[i] - by)
  dx.append(tdx)
  dy.append(tdy)
  distance.append(tdx + tdy)
  i += 1
  

for row in range(0, 4000001):
  intervals = []
  for i in range(0, len(sx)):
    if sy[i] < row and sy[i] + distance[i] < row: continue
    if sy[i] > row and sy[i] - distance[i] > row: continue
    dist_to_row = abs(row - sy[i])
    width = distance[i] - dist_to_row
    low = max(sx[i]-width, 0)
    high = min(sx[i]+width, 4000000)
    intervals.append([low, high])
  rtn = mergeIntervals(intervals)
  if len(rtn) > 1:
    low = rtn[0][1] + 1
    high = rtn[1][0] - 1
    print("x = %d / %d" % (low, high))
    print("Freq = %d" % freq(low, row))
    assert(low == high)
    assert(len(rtn)==2)
    break
