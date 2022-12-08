#!/usr/bin/python3

import os

with open("input.day8.txt", "r") as f:
  all = f.readlines()

MAX_X = len(all[0]) - 2
MAX_Y = len(all) - 1

print("Grid is %d x %d" % (MAX_X + 1, MAX_Y + 1))


def treesVisible(x, y):
  ht = all[y][x]

  if x == 0 or y == 0 or x == MAX_X or y == MAX_Y:
    return 0

  #print("Checking (%d, %d): %s" % (x, y, all[y][x]))

  west = 0
  for i in range(x-1, -1, -1):
    west += 1
    if all[y][i] >= ht:
      break
  #print("To west: %d" % west)

  north = 0
  for i in range(y-1, -1, -1):
    north += 1
    if all[i][x] >= ht:
      break
  #print("To north: %d" % north)

  east = 0
  for i in range(x+1, MAX_X+1):
    east += 1
    if all[y][i] >= ht:
      break
  #print("To east: %d" % east)

  south = 0
  for i in range(y+1, MAX_Y+1):
    south += 1
    if all[i][x] >= ht:
      break
  #print("To south: %d" % south)

  return west * north * east * south
  
max_visible = 0

for y in range(0, MAX_Y + 1):
  for x in range(0, MAX_X + 1):
    trees = treesVisible(x, y)
    if trees > max_visible:
      max_visible = trees

print("Visible = %d" % max_visible)
