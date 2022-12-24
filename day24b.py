#!/usr/bin/python3

import sys

with open("input.day24.txt", "r") as f:
  all = f.readlines()

mymap = []
bliz = []

moves = [
            (-1, 0),
  ( 0, -1), ( 0, 0), ( 0, 1),
            ( 1, 0),
]

delta = {
  '>': ( 0,  1),
  '<': ( 0, -1),
  '^': (-1,  0),
  'v': ( 1,  0),
}

class Blizzard:
  def __init__(self, y, x, dir):
    self.y = y
    self.x = x
    self.dir = dir
    self.dy, self.dx = delta[dir]

  def move(self):
    self.y += self.dy
    self.y %= final_y
    self.x += self.dx
    self.x %= final_x + 1 
    
    return self.y, self.x, self.dir

  def get_yx(self):
    return (self.y, self.x)

start_y = -1
start_x = all[0].index('.') - 1
current_locs = [(start_y, start_x)]
final_y = len(all) - 2
final_x = all[-1].index('.') - 1
start = (start_y, start_x)
final = (final_y, final_x)
special = [start, final]

mymap = []

for line in all[1:len(all)-1]:
  mymap.append(line.strip('#\n'))


def print_map():
  print('#%s.' % (' ' * (current_x)))
  for line in mymap: print('#%s' % ''.join(line))
  print('#%s.' % (' ' * (final_x)))


def gen_new_locs(locs):
  rtn = []
  for y, x in locs:
    for dy, dx in moves:
      ty = y + dy
      tx = x + dx
      loc = (ty, tx) 
      if loc not in special: 
        if tx < 0 or ty < 0 or tx > final_x or ty > final_y - 1:
          continue
      rtn.append(loc)
  return rtn

for y in range(len(mymap)):
  for x in range(len(mymap[y])):
    if mymap[y][x] == '.': continue
    bliz.append(Blizzard(y, x, mymap[y][x]))

got_thru = False
got_snax = False

rounds = 0
while True:
  rounds += 1
  new_locs = gen_new_locs(current_locs)
  blocked = set()
  for b in bliz:
    y, x, d = b.move()
    blocked.add((y, x))
  current_locs = set()
  for loc in new_locs:
    if loc not in blocked:
      current_locs.add(loc)
  if final in current_locs:
    if got_snax:
      print('Got out with snacks in round %d' % rounds)
      sys.exit(0)
    elif got_thru:
      pass
    else:
      got_thru = True
      current_locs = {final}
      print('Got out without snacks in round %d' % rounds)
  if start in current_locs:
    if got_snax: continue
    if got_thru:
      got_snax = True
      current_locs = {start}
      print('Got snacks in round %d' % rounds)
