#!/usr/bin/python3

import os

with open("input.day9.txt", "r") as f:
  all = f.readlines()

visited = set()

h_x = 0
h_y = 0
t_x = 0
t_y = 0

def move(dir):
  global h_x
  global h_y
  global t_x
  global t_y
  if dir == "R":
    h_x += 1
  if dir == "U":
    h_y += 1
  if dir == "L":
    h_x -= 1
  if dir == "D":
    h_y -= 1

  d_x = h_x - t_x
  d_y = h_y - t_y
  if abs(d_x) >= 2 or abs(d_y) >= 2:
    if d_x != 0: t_x += d_x / abs(d_x)
    if d_y != 0: t_y += d_y / abs(d_y)
  visited.add("%d:%d" % (t_x, t_y))


def moveN(dir, num):
  for _ in range(0, int(num)):
    move(dir) 


for line in all:
  l = line.strip()
  args = line.split(" ")
  moveN(args[0], args[1])
 
print("Visited spots = %d" % len(visited))
