#!/usr/bin/python3

import sys

with open("input.day17.test", "r") as f:
  all = f.readlines()

pieces = [ 0x000000f0, 0x0040e040, 0x002020e0, 0x80808080, 0x0000c0c0 ]

width = [4, 3, 3, 1, 2]
right_limit = [3, 4, 4, 6, 5]

empty = 0b00000000
floor = 0b01111111
assert(len(all) == 1)
input = all[0].strip()
wind = 0
cave = bytearray(10)
cave[0] = floor
piece_in_flight = 0
height = 4
left = 2
cave_height = 0

def write_cave(count):
  f = open('b_%04d.txt' % count, 'w')
  for l in range(len(cave)-1, -1, -1):
    f.write('{0:4d}: |{1:08b}|\n'.format(l, cave[l]))
  f.close()

def print_cave():
  for l in range(len(cave)-1, -1, -1):
    print('{0:4d}: |{1:07b}|'.format(l, cave[l]))

def check_collision(cave, piece_id, ht, left):
  cave_map = ((((cave[ht+3] << 8 | cave[ht+2]) << 8) | cave[ht+1]) << 8) | cave[ht+0]
  # cave_map = int.from_bytes(cave_bytes, 'little')
  #print('Height: %d' % ht)
  #print('Cave map value: {0:032b}'.format(cave_map))
  rock_map = pieces[piece_id] >> left+1
  #print('Rock map value: {0:032b}'.format(rock_map))
  check = cave_map & rock_map
  #print('DEBUG: Check = %d' % check)
  return check != 0

def place_piece_in_cave(piece_id, ht, left):
  global cave
  #for i in range(0, 4):
  #  print('Cave {0}: {1:b}'.format(i, cave[i]))
  cave_map = ((((cave[ht+3] << 8 | cave[ht+2]) << 8) | cave[ht+1]) << 8) | cave[ht+0]
  #print('Cave map value: %d' % cave_map)
  rock_map = pieces[piece_id] >> left+1
  #print('Rock map value: %d' % rock_map)
  check = cave_map | rock_map
  #print('DEBUG: Check = %d' % check)
  hiq = (check & 0xff000000) >> 24
  hlq = (check & 0x00ff0000) >> 16
  lhq = (check & 0x0000ff00) >> 8
  loq = (check & 0x000000ff)
  cave[ht] = loq
  cave[ht+1] = lhq
  cave[ht+2] = hlq
  cave[ht+3] = hiq

def repeater(s):
  i = (s+s)[1:-1].find(s)
  if i == -1:
    return s
  else:
    return s[:i+1]

def has_cycle():
  # if len(cave) <= 5000: return False
  cavestr = cave.decode('utf-8')
  test_string = cavestr[-100:]
  length = len(cavestr)
  start = length - 100
  first_match = cavestr.find(test_string)
  print('Estimated start = %d' % start)
  print('First match = %d' % first_match)
  if abs(first_match - start) < 3: return False
  print('Computed repeat length = %d' % (start - first_match))
  sys.exit(0)
  #out = repeater(test_string)
  #print('Test: input length = %d' % len(test_string))
  #print('Test: output length = %d' % len(out))
  #if len(test_string) == len(out): return False
  #return len(test_string) - len(out) < len(out)


count = 0
while count < 10000000000000:
  wind_dir = input[wind]
  test_left = -1
  if wind_dir == '<':
    test_left = max(0, left - 1)
  else:
    test_left = min(left + 1, right_limit[piece_in_flight])
  assert(test_left != -1)
  if not check_collision(cave, piece_in_flight, height, test_left):
    left = test_left
  #print('Wind = %d, Left = %d' % (wind, left))
  wind += 1
  wind %= len(input)

  test_height = height - 1
  if not check_collision(cave, piece_in_flight, test_height, left):
    height = test_height
    #print('New height = %d' % height)
  else:
    count += 1
    place_piece_in_cave(piece_in_flight, height, left)
    #print_cave()
    if count % 10000 == 0:
      if has_cycle(): break
    
    piece_in_flight += 1
    piece_in_flight %= len(pieces)

    height = len(cave) - 1
    while cave[height] == empty:
      height -= 1
    height += 4 
    left = 2
    while len(cave) <= height+4:
      cave.append(empty)

    

#print_cave(cave)
h = len(cave)
while h >=0:
  h -= 1
  if cave[h] != 0:
    print('Height is %d' % h)
    break
