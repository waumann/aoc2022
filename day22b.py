#!/usr/bin/python3

import copy
import sys

with open("input.day22.txt", "r") as f:
  all = f.readlines()

EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3

marks = {
  EAST: '>',
  SOUTH: 'v',
  WEST: '<',
  NORTH: '^',
}

direction = {
  EAST: 'east',
  SOUTH: 'south',
  WEST: 'west',
  NORTH: 'north',
}

maxlen = 0
tmp = list()
for line in all:
  stripped = line.rstrip()
  if len(stripped) > maxlen: maxlen = len(stripped)
  tmp.append(list(stripped))

for l in tmp:
  if len(l) < maxlen:
    l.extend(' ' * (maxlen - len(l)))

mymap = tmp[:-2]
annotated = copy.deepcopy(mymap)
maxht = len(mymap)

#print('Max y = %d' % len(mymap))

def print_map(row, col):
  for y in range(row-8, row+9):
    out = ''
    rr = y % maxht
    for x in range(col-8, col+9):
      cc = x % maxlen
      out = out + annotated[rr][cc]
    print(out)
  #for line in annotated:
  #  print(''.join(line))
  #print('=' * len(annotated[0]))

def parse_directions(input):
  rtn = list()
  dist = 0
  for i in range(len(input.rstrip())):
    ch = input[i]
    if ch.isdigit():
      dist = dist * 10 + int(ch)
    else:
      rtn.append(dist)
      rtn.append(ch)
      dist = 0
  rtn.append(dist)
  return rtn


def do_move(y, x, dir):
  msg = ''
  newx = None
  newy = None
  newdir = None
  if dir == EAST:
    if x+1 == len(mymap[y]) or mymap[y][x+1] == ' ':
      if x == 149 and y <= 49:  ## Right of 2 wraps to right of 6, inv
        newdir = WEST
        newx = 99 
        newy = 149 - y
        msg = 'Could not 2 -> 6 from (%d, %d) %s' % (x, y, direction[dir])
      elif x == 99 and y <= 99:  ## Right of 4 wraps to bottom of 2
        newdir = NORTH
        newx = y + 50
        newy = 49
        msg = 'Could not 4 -> 2 from (%d, %d) %s' % (x, y, direction[dir])
      elif x == 99 and y <= 149:  ## Right of 6 wraps to right of 2, inv
        newdir = WEST
        newx = 149
        newy = 149 - y
        msg = 'Could not 6 -> 2 from (%d, %d) %s' % (x, y, direction[dir])
      elif x == 49 and y >= 150:  ## Right of 3 wraps to bottom of 6
        newdir = NORTH
        newx = y - 100
        newy = 149
        msg = 'Could not 3 -> 6 from (%d, %d) %s' % (x, y, direction[dir])
      if newx != None and newy != None and newdir != None:
        if mymap[newy][newx] == '.': return (newy, newx, newdir)
        if mymap[newy][newx] == '#': return (y, x, dir)
        print(msg)
        print('Proposed new is (%d, %d) %s.' % (newx, newy, direction[newdir]))
        sys.exit(0)
      print('Unknown wrap from (%d, %d) facing %s' % (x, y, direction[dir]))
      sys.exit(0)
    if mymap[y][x+1] == '.': return (y, x+1, dir)
    if mymap[y][x+1] == '#': return (y, x, dir)
    print('Unexpected condition in EAST')
    sys.exit(0)
  if dir == WEST:
    if x == 0 or mymap[y][x-1] == ' ':
      if x == 50 and y <= 49:  ## Left of 1 wraps to left of 5, inv
        newdir = EAST
        newx = 0
        newy = 149 - y
        msg = 'Could not 1 -> 5 from (%d, %d) %s' % (x, y, direction[dir])
      elif x == 50 and y <= 99:  ## Left of 4 wraps to top of 5
        newdir = SOUTH
        newx = y - 50
        newy = 100
        msg = 'Could not 4 -> 5 from (%d, %d) %s' % (x, y, direction[dir])
      elif x == 0 and y <= 149:  ## Left of 5 wraps to left of 1, inv
        newdir = EAST
        newx = 50
        newy = 149 - y
        msg = 'Could not 5 -> 1 from (%d, %d) %s' % (x, y, direction[dir])
      elif x == 0 and y >= 150:  ## Left of 3 wraps to top of 1
        newdir = SOUTH
        newx = y - 100
        newy = 0
        msg = 'Could not 3 -> 1 from (%d, %d) %s' % (x, y, direction[dir])
      if newx != None and newy != None and newdir != None:
        if mymap[newy][newx] == '.': return (newy, newx, newdir)
        if mymap[newy][newx] == '#': return (y, x, dir)
        print(msg)
        print('Proposed new is (%d, %d) %s.' % (newx, newy, direction[newdir]))
        sys.exit(0)
      print('Unknown wrap from (%d, %d) facing %s' % (x, y, direction[dir]))
      sys.exit(0)
    if mymap[y][x-1] == '.': return (y, x-1, dir)
    if mymap[y][x-1] == '#': return (y, x, dir)
    print('Unexpected condition in WEST')
    sys.exit(0)
  if dir == NORTH:
    if y == 0 or mymap[y-1][x] == ' ':
      if x <= 99 and y == 0:  ## Top of 1 wraps to left of 3
        newdir = EAST
        newx = 0
        newy = x + 100
        msg = 'Could not 1 -> 3 from (%d, %d) %s' % (x, y, direction[dir])
      elif x >= 100 and y == 0:  ## Top of 2 wraps to bottom of 3
        newdir = NORTH
        newx = x - 100
        newy = 199
        msg = 'Could not 2 -> 3 from (%d, %d) %s' % (x, y, direction[dir])
      elif x <= 49 and y == 100:  ## Top of 5 wraps to left of 4
        newdir = EAST
        newx = 50
        newy = x + 50
        msg = 'Could not 5 -> 4 from (%d, %d) %s' % (x, y, direction[dir])
      if newx != None and newy != None and newdir != None:
        if mymap[newy][newx] == '.': return (newy, newx, newdir)
        if mymap[newy][newx] == '#': return (y, x, dir)
        print(msg)
        print('Proposed new is (%d, %d) %s.' % (newx, newy, direction[newdir]))
        sys.exit(0)
      print('Unknown wrap from (%d, %d) facing %s' % (x, y, direction[dir]))
      sys.exit(0)
    if mymap[y-1][x] == '.': return (y-1, x, dir)
    if mymap[y-1][x] == '#': return (y, x, dir)
    print('Unexpected condition in NORTH')
    sys.exit(0)
  if dir == SOUTH:
    if y+1 == len(mymap) or mymap[y+1][x] == ' ':
      if x >= 100 and y == 49:  ## Bottom of 2 wraps to right of 4
        newdir = WEST
        newx = 99
        newy = x - 50
        msg = 'Could not 2 -> 4 from (%d, %d) %s' % (x, y, direction[dir])
      elif x >= 50 and x <= 99 and y == 149:  ## Bottom of 6 wraps to right of 3
        newdir = WEST
        newx = 49
        newy = x + 100
        msg = 'Could not 6 -> 3 from (%d, %d) %s' % (x, y, direction[dir])
      elif x <= 49 and y == 199:  ## Bottom of 3 wraps to top of 2
        newdir = SOUTH
        newx = x + 100
        newy = 0
        msg = 'Could not 3 -> 2 from (%d, %d) %s' % (x, y, direction[dir])
      if newx != None and newy != None and newdir != None:
        if mymap[newy][newx] == '.': return (newy, newx, newdir)
        if mymap[newy][newx] == '#': return (y, x, dir)
        print(msg)
        print('Proposed new is (%d, %d) %s.' % (newx, newy, direction[newdir]))
        sys.exit(0)
      print('Unknown wrap from (%d, %d) facing %s' % (x, y, direction[dir]))
      sys.exit(0)

    if mymap[y+1][x] == '.': return (y+1, x, dir)
    if mymap[y+1][x] == '#': return (y, x, dir)
    print('Unexpected condition in SOUTH')
    sys.exit(0)
  print('Unknown facing value %d' % dir)
  sys.exit(0)

row = 0
col = mymap[row].index('.')
facing = EAST
annotated[row][col] = marks[facing]

dirs = parse_directions(all[-1])

# print_map(row, col)

for d in dirs:
  if isinstance(d, int):
    #print('DEBUG: Moving %d units in direction %s' % (d, direction[facing]))
    for _ in range(0, d):
      row, col, facing = do_move(row, col, facing)
      # print('DEBUG: row == %d, col == %d' % (row, col))
      annotated[row][col] = marks[facing]
      #print('Now at (%d, %d) facing %s' % (col, row, direction[facing]))
      #print_map(row, col)
  else:
    #print('DEBUG: facing change: %s' % d)
    if d == 'L': facing -= 1
    elif d == 'R': facing += 1
    else:
      print('Unknown direction "%s"' % d)
      sys.exit(0)
    facing %= 4
    annotated[row][col] = marks[facing]
    #print('Now at (%d, %d) facing %s' % (col, row, direction[facing]))
    #print_map(row, col)

#print_map(row, col)

print('Password = 1000 * %d + 4 * %d + %d = %d' % (
    row+1, col+1, facing, 1000 * (row+1) + 4 * (col+1) + facing))
print('78231 is too low')
