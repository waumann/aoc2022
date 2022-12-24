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

mymap = []

for line in all[1:len(all)-1]:
  mymap.append(line.strip('#\n'))


def print_map():
  print('#%s.' % (' ' * (current_x)))
  for line in mymap: print('#%s' % ''.join(line))
  print('#%s.' % (' ' * (final_x)))

for y in range(len(mymap)):
  for x in range(len(mymap[y])):
    if mymap[y][x] == '.': continue
    bliz.append(Blizzard(y, x, mymap[y][x]))

turns = 0
while True:
  turns += 1
  if turns % 100 == 0:
    print('Number of possible locations: %d' % len(current_locs))
  if (final_y-1, final_x) in current_locs:
    print('Exit reached at turn %d' % turns)
    sys.exit(0) 
  for y in range(len(mymap)):
    mymap[y] = ['.' for _ in range(final_x + 1)]
  for b in bliz:
    y, x, d = b.move()
    if mymap[y][x] == '.':
      mymap[y][x] = d
    elif mymap[y][x].isdigit():
      mymap[y][x] = str(int(mymap[y][x]) + 1)
    else:
      mymap[y][x] = '2'
  new_locs = []
  for y, x in current_locs:
    for dy, dx in moves:
      ty = y + dy
      tx = x + dx
      if tx < 0 or ty < 0 or tx > final_x or ty > final_y - 1:
        if tx != start_x or ty != start_y: continue
      print('Candidate location: (%d, %d)' % (ty, tx))
      if ty == start_y or mymap[ty][tx] == '.':
        if (ty, tx) not in new_locs:
          new_locs.append((ty, tx))
  current_locs = new_locs 
