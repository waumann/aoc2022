#!/usr/bin/python3

import sys
import binascii

with open("input.day17.txt", "r") as f:
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
heights = {}
cycle_test = {}

def write_cave(count):
  f = open('b_%04d.txt' % count, 'w')
  for l in range(len(cave)-1, -1, -1):
    f.write('{0:4d}: |{1:08b}|\n'.format(l, cave[l]))
  f.close()

def print_cave():
  max = 20
  for l in range(len(cave)-1, -1, -1):
    print('%8d: |%s|' % (l, '{1:07b}'.format(l, cave[l]).replace('1', '#').replace('0', '.')))
    max -= 1
    if max == 0: return

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
  #for i in range(4):
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

def do_wind(left, wind, piece_in_flight, height):
  wind_dir = input[wind]
  test_left = -1
  if wind_dir == '<':
    test_left = max(0, left - 1)
  else:
    test_left = min(left + 1, right_limit[piece_in_flight])
  if not check_collision(cave, piece_in_flight, height, test_left):
    left = test_left
  return left

def has_cycle(c, ht):
  key = 0
  if ht < 32: return None
  for b in range(15, -1, -1):
    h = ht - b * 4
    cave_map = ((((cave[h] << 8 | cave[h-1]) << 8) | cave[h-2]) << 8) | cave[h-3]
    key = key << 32
    key = key | cave_map
    #print('DEBUG: %d: %x' % (b, key))
  #print('DEBUG: Setting cycle key to %d' % key)
  if c < 100: return None
  if key in cycle_test:
    print('%d: Found cycle, returning %d' % (c, cycle_test[key]))
    return cycle_test[key]
  cycle_test[key] = c
  return None
  

ITERS = 1000000000000

count = 0
bonus_count = 0
bonus_height = 0
cycle_found = False
cur_drop = 0

while count + bonus_count < ITERS:
  left = do_wind(left, wind, piece_in_flight, height)
  wind += 1
  wind %= len(input)

  # Process drop
  test_height = height - 1
  if not check_collision(cave, piece_in_flight, test_height, left):
    height = test_height
    cur_drop += 1
    continue

  # Stick piece in place
  count += 1
  place_piece_in_cave(piece_in_flight, height, left)

  # Update to new piece
  piece_in_flight += 1
  piece_in_flight %= len(pieces)

  # Save height with piece in place
  h = len(cave)-1
  while cave[h] == empty:
    h -= 1
  heights[count] = h

  # Set values for next piece
  height = h + 4
  while len(cave) <= height + 4:
    cave.append(empty)
  left = 2

  if cycle_found: continue

  cycle_point = has_cycle(count, h)
  # Still no cycle, save what this looks like
  if cycle_point is None:
    continue
  cycle_found = True
  cycle_length = count - cycle_point
  print('Cycle length: %d - %d = %d' % (count, cycle_point, cycle_length))
  cycles = int((ITERS - count) / cycle_length)
  print('Adding bonus of %d cycles.' % cycles)
  bonus_count = cycles * cycle_length
  print('  Bonus count = %d' % bonus_count)
  bonus_height = cycles * (h - heights[cycle_point])
  print('  Bonus height = %d' % bonus_height)

h = len(cave)
while h >=0:
  h -= 1
  if cave[h] != 0:
    print('Height is %d' % (h + bonus_height))
    break

15142857142861
1514285714288



