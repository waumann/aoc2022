#!/usr/bin/python3

import os

with open("input.day9.txt", "r") as f:
  all = f.readlines()

visited = set()

x = list()
y = list()
for _ in range(0, 10):
  x.append(0)
  y.append(0)

def follow(n):
  d_x = x[n-1] - x[n]
  d_y = y[n-1] - y[n]
  if abs(d_x) >= 2 or abs(d_y) >= 2:
    if d_x != 0: x[n] += d_x / abs(d_x)
    if d_y != 0: y[n] += d_y / abs(d_y)

  if n == 9:
    visited.add("%d:%d" % (x[9], y[9]))
  else:
    follow(n+1)
    
def move(dir):
  global x
  global y
  if dir == "R":
    x[0] += 1
  if dir == "U":
    y[0] += 1
  if dir == "L":
    x[0] -= 1
  if dir == "D":
    y[0] -= 1
  follow(1)


def moveHead(dir, num):
  for _ in range(0, int(num)):
    move(dir) 

for line in all:
  l = line.strip()
  args = line.split(" ")
  moveHead(args[0], args[1])
 
print("Visited spots = %d" % len(visited))
