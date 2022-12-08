#!/usr/bin/python3

import os

with open("input.day8.txt", "r") as f:
  all = f.readlines()

MAX_X = len(all[0]) - 2
MAX_Y = len(all) - 1

print("Grid is %d x %d" % (MAX_X + 1, MAX_Y + 1))


def isVisible(x, y):
  ht = all[y][x]
  if x == 0 or y == 0 or x == MAX_X or y == MAX_Y:
    return True

  # print("Evaluating (%d, %d): %s" % (x, y, ht))
  is_visible = True
  for i in range(0, x):
    if all[y][i] >= ht:
      is_visible = False
      break
  if is_visible:
    # print("Visible from west")
    return True

  is_visible = True
  for i in range(0, y):
    if all[i][x] >= ht:
      is_visible = False
      break
  if is_visible:
    # print("Visible from north")
    return True

  is_visible = True
  for i in range(x + 1, MAX_X + 1):
    # print("Checking (%d, %d): %s" % (i, y, all[y][i]))
    if all[y][i] >= ht:
      is_visible = False
      break
  if is_visible:
    # print("Visible from east")
    return True

  is_visible = True
  for i in range(y + 1, MAX_Y + 1):
    if all[i][x] >= ht:
      is_visible = False
      break
  if is_visible:
    # print("Visible from south")
    return True

  return False
  
visible = 0

for y in range(0, MAX_Y + 1):
  for x in range(0, MAX_X + 1):
    if isVisible(x, y):
      visible += 1

print("Visible = %d" % visible)
