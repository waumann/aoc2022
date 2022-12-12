#!/usr/bin/python3

import sys

with open("input.day12.txt", "r") as f:
  all = f.readlines()

moved = set()

MAX_X = len(all[0]) - 2
MAX_Y = len(all) - 1

print("Grid is %d x %d" % (MAX_X + 1, MAX_Y + 1)) 
def getHeight(x, y):
  height = ord(all[y][x])
  if height == 83:
    height = ord("a")
  if height == 69:
    height = ord("z")
  return height


def dprint(x, y, str):
  if x == 4 and y == 0:
    print(str)

class Route:
  def __init__(self, x, y, steps):
    self.x = x
    self.y = y
    self.steps = steps

  def do_move(self):
    global all
    rtnlist = []
    height = getHeight(self.x, self.y)
    # print("Starting with (%d, %d) => %d" % (self.x, self.y, height))
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
      nx = self.x + dx
      ny = self.y + dy
      # dprint(self.x, self.y, "Trying (%d, %d)" % (nx, ny))
      if nx < 0: continue
      if ny < 0: continue
      if nx > MAX_X: continue
      if ny > MAX_Y: continue
      # dprint(self.x, self.y, "(%d, %d) is in bounds" % (nx, ny))
      key = nx * 1000 + ny
      if not key in moved:
        rise = getHeight(nx, ny) - height
        if rise <= 1:
          moved.add(key)
          new = Route(nx, ny, self.steps + 1)
          rtnlist.append(new)
      else:
        pass
        # dprint(self.x, self.y, "(%d, %d) already tried" % (nx, ny))
    return rtnlist


s_x = -1
s_y = -1
e_x = -1
e_y = -1

for y in range(0, MAX_Y + 1):
  for x in range(0, MAX_X + 1):
    if all[y][x] == 'S':
      s_x = x
      s_y = y
    if all[y][x] == 'E':
      e_x = x
      e_y = y

print("Target is (%d, %d)" % (e_x, e_y))

start = Route(s_x, s_y, 0)
key = s_x * 1000 + s_y
moved.add(key)

workq = [start]

while True:
  next = workq.pop(0)
  moves = next.do_move()
  for move in moves:
    # print("Moved to (%d, %d)" % (move.x, move.y))
    if move.x == e_x and move.y == e_y:
      print("Total moves: %d" % move.steps)
      sys.exit(0)
  workq += moves
  # print("Queue length: %d" % len(workq))
