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
  if dir == EAST:
    if x+1 == len(mymap[y]) or mymap[y][x+1] == ' ':
      for i in range(len(mymap[y])):
        if mymap[y][i] == ' ': continue
        if mymap[y][i] == '.': return (y, i)
        if mymap[y][i] == '#': return (y, x)
      print('Could not find a valid location in row %d' % y)
      sys.exit(0)
    if mymap[y][x+1] == '.': return (y, x+1)
    if mymap[y][x+1] == '#': return (y, x)
    print('Unexpected condition in EAST')
    sys.exit(0)
  if dir == WEST:
    if x == 0 or mymap[y][x-1] == ' ':
      for i in range(len(mymap[y])-1, -1, -1):
        if mymap[y][i] == ' ': continue
        if mymap[y][i] == '.': return (y, i)
        if mymap[y][i] == '#': return (y, x)
      print('Could not find a valid location in row %d' % y)
      sys.exit(0)
    if mymap[y][x-1] == '.': return (y, x-1)
    if mymap[y][x-1] == '#': return (y, x)
    print('Unexpected condition in WEST')
    sys.exit(0)
  if dir == NORTH:
    if y == 0 or mymap[y-1][x] == ' ':
      for i in range(len(mymap)-1, -1, -1):
        if mymap[i][x] == ' ': continue
        if mymap[i][x] == '.': return (i, x)
        if mymap[i][x] == '#': return (y, x)
      print('Could not find a valid location in column %d' % x)
      sys.exit(0)
    if mymap[y-1][x] == '.': return (y-1, x)
    if mymap[y-1][x] == '#': return (y, x)
    print('Unexpected condition in NORTH')
    sys.exit(0)
  if dir == SOUTH:
    if y+1 == len(mymap) or mymap[y+1][x] == ' ':
      for i in range(len(mymap)):
        if mymap[i][x] == ' ': continue
        if mymap[i][x] == '.': return (i, x)
        if mymap[i][x] == '#': return (y, x)
      print('Could not find a valid location in column %d' % x)
      sys.exit(0)
    if mymap[y+1][x] == '.': return (y+1, x)
    if mymap[y+1][x] == '#': return (y, x)
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
      row, col = do_move(row, col, facing)
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
print('7299 is too low')
