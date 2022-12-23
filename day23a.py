#!/usr/bin/python3

from datetime import datetime

with open("input.day23.txt", "r") as f:
  all = f.readlines()

mymap = []
elves = []

directions = ['N', 'S', 'W', 'E']

check_spread = [
  (-1, -1), (-1, 0), (-1, 1),
  ( 0, -1),          ( 0, 1),
  ( 1, -1), ( 1, 0), ( 1, 1),
]

check_dir = {
  'N': [(-1, -1), (-1,  0), (-1,  1)],
  'S': [( 1, -1), ( 1,  0), ( 1,  1)],
  'E': [(-1,  1), ( 0,  1), ( 1,  1)],
  'W': [(-1, -1), ( 0, -1), ( 1, -1)],
}

prop_dir = {
  'N': (-1,  0),
  'S': ( 1,  0),
  'E': ( 0,  1),
  'W': (-0, -1),
}


for line in all:
  mymap.append(list(line.rstrip()))

for y in range(len(mymap)):
  for x in range(len(mymap[y])):
    if mymap[y][x] == '#':
      elves.append((y,x))

def get_adjacent(elf):
  adj = []
  ey, ex = elf
  for fy, fx in elves:
    if ey == fy and ex == fx: continue
    if abs(ex - fx) <= 1 and abs(ey - fy) <= 1:
      adj.append((fy-ey, fx-ex))
  return adj
  
def not_spread_out():
  for e in elves:
    adj = get_adjacent(e)
    if len(adj) > 0: return True
  return False
      

def make_proposals():
  props = dict()
  for e in elves:
    ey, ex = e
    adj = get_adjacent(e)
    #print('Elf at %d, %d has adjacencies %s.' % (ey, ex, adj))
    #print_map(e)
    if len(adj) == 0: continue
    for dir in directions:
      blocked = False
      #print('Checking %s' % dir)
      for delta in check_dir[dir]:
        #print('Check if %s in %s' % (delta, adj))
        if delta in adj: blocked = True
      if blocked: continue
      ey, ex = e
      dy, dx = prop_dir[dir]
      prop = (ey + dy, ex + dx)
      #print('Proposing %s for %s.' % (prop, e))
      props.setdefault(prop, [])
      props[prop].append(e)
      break
  return props


def process_proposals(props):
  for k, v in props.items():
    if len(v) == 1:
      ny, nx = k
      y, x = v[0]
      #print('Elf at %d, %d moves to %d, %d.' % (y, x, ny, nx))
      #print('Before:')
      #print_map(hilite=v[0])
      elves.remove(v[0])
      elves.append(k)
      #print('After:')
      #print_map(hilite=k)
      
def get_min_and_max():
  min_y, min_x = elves[0]
  max_y, max_x = elves[0]
  # print('Elf: %d, %d' % (min_y, min_x))

  for y, x in elves[1:]:
    # print('Elf: %d, %d' % (y, x))
    if y < min_y: min_y = y
    if y > max_y: max_y = y
    if x < min_x: min_x = x
    if x > max_x: max_x = x

  return (min_y, max_y, min_x, max_x)


def print_map(hilite=None):
  min_y, max_y, min_x, max_x = get_min_and_max()
  # print('Y spans %d to %d' % (min_y, max_y))
  # print('X spans %d to %d' % (min_x, max_x))
  y_offset = -min_y  ### Add this to elf y values
  x_offset = -min_x  ### Add this to elf x values
  row = ['.' for x in range(min_x, max_x+1)]
  mymap = [row.copy() for y in range(min_y, max_y+1)]
  # print('Map size = %d x %d' % (len(mymap), len(mymap[0])))
  # print('Y, X offsets = %d, %d' % (y_offset, x_offset))
  for ey, ex in elves: mymap[ey+y_offset][ex+x_offset] = '#'
  if hilite:
    hy, hx = hilite
    mymap[hy+y_offset][hx+x_offset] = '@'
  for line in mymap: print(''.join(line))
  print()
  
#print('== Initial State ==')
#print_map()
min_y, max_y, min_x, max_x = get_min_and_max()
dx = max_x - min_x + 1
dy = max_y - min_y + 1
area = dy * dx
empty = area - len(elves)
print('Answer: %d x %d = %d, %d - %d = %d' % (dy, dx, area, area, len(elves), empty))
rnum = 1
while not_spread_out():
  proposed = make_proposals()
  process_proposals(proposed)
  directions.append(directions.pop(0))
  #print('== End of Round %d ==' % rnum)
  #print_map()
  if rnum == 10: break
  rnum += 1
  if rnum % 10 == 0:
    min_y, max_y, min_x, max_x = get_min_and_max()
    dx = max_x - min_x + 1
    dy = max_y - min_y + 1
    area = dy * dx
    empty = area - len(elves)
    print('Round %d (%s): %d x %d = %d, %d - %d = %d' % (rnum, datetime.now().strftime("%H:%M:%S"), dy, dx, area, area, len(elves), empty))

min_y, max_y, min_x, max_x = get_min_and_max()

dx = max_x - min_x + 1
dy = max_y - min_y + 1
area = dy * dx
empty = area - len(elves)
print('Answer: %d x %d = %d, %d - %d = %d' % (dy, dx, area, area, len(elves), empty))
print('17046 is too high.')
