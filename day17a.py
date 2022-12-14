#!/usr/bin/python3

import copy

with open("input.day17.txt", "r") as f:
  all = f.readlines()

pieces = [{
  'width': 4,
  'height': 1,
  'text': ['####']
}, {
  'width': 3,
  'height': 3,
  'text': [' # ', '###', ' # ']
}, {
  'width': 3,
  'height': 3,
  'text': ['###', '  #', '  #']
}, {
  'width': 1,
  'height': 4,
  'text': ['#', '#', '#', '#']
}, {
  'width': 2,
  'height': 2,
  'text': ['##', '##']
}]

empty = ['.', '.', '.', '.', '.', '.', '.']
floor = ['#', '#', '#', '#', '#', '#', '#']
assert(len(all) == 1)
input = all[0].strip()
wind = 0
cave = [floor, empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy()]
piece_in_flight = 0
height = 4
left = 2
cave_height = 0

def print_cave(count):
  f = open('a_%04d.txt' % count, 'w')
  for l in range(len(cave)-1, -1, -1):
    out = ''.join(cave[l])
    out = out.replace('.', '0')
    out = out.replace('#', '1')
    f.write('{0:4d}: |{1:s}0|\n'.format(l, out))
  f.close()

def check_collision(cave, piece_id, ht, left):
  for piece_h in range(0, pieces[piece_id]['height']):
    for piece_x in range(0, pieces[piece_id]['width']):
      if pieces[piece_id]['text'][piece_h][piece_x] == "#":
        #print('DEBUG: height goes to %d' % len(cave))
        #print('DEBUG: height = %d, piece_h = %d, index = %d' % (ht, piece_h, ht + piece_h - 1))
        #print('DEBUG: left = %d, piece_x = %d' % (left, piece_x))
        #print('CAVE: %s' % cave[ht+piece_h])
        y = ht + piece_h
        x = left + piece_x
        #print('DEBUG: Checking (%d, %d)' % (x, y))
        if cave[y][x] == "#":
          #print('Collision at (%d, %d)' % (x, y))
          return True
  return False

def place_piece_in_cave(cave, piece_in_flight, height, left, use_char):
  for piece_h in range(0, pieces[piece_in_flight]['height']):
    for piece_x in range(0, len(pieces[piece_in_flight]['text'][piece_h])):
      if pieces[piece_in_flight]['text'][piece_h][piece_x] == '#':
        assert(cave[height+piece_h][left+piece_x] == '.')
        cave_alt = height + piece_h
        cave[cave_alt][left + piece_x] = use_char
  return(cave)


#disp = place_piece_in_cave(copy.deepcopy(cave), piece_in_flight, height, left, '@')
#print_cave(disp)
count = 0
while count < 2022:
  #print_cave(
  #   place_piece_in_cave(
  #       copy.deepcopy(cave), piece_in_flight, height, left, '@'))
  wind_dir = input[wind]
  #print('Wind: %s' % wind_dir)
  test_left = -1
  if wind_dir == '<':
    test_left = max(0, left - 1)
  else:
    test_left = min(left + 1, 7 - pieces[piece_in_flight]['width'])
  assert(test_left != -1)
  if not check_collision(cave, piece_in_flight, height, test_left):
    left = test_left
  #print('Wind index was %d' % wind)
  #print('Wind = %d, Left = %d' % (wind, left))
  wind += 1
  wind %= len(input)
  #print('Wind index is now %d (%d)' % (wind, len(input)))
  #disp = place_piece_in_cave(copy.deepcopy(cave), piece_in_flight, height, left, '@')
  #print_cave(disp)

  #print('Drop:')
  test_height = height - 1
  if not check_collision(cave, piece_in_flight, test_height, left):
    height = test_height
    #disp = place_piece_in_cave(copy.deepcopy(cave), piece_in_flight, height, left, '@')
    #print_cave(disp)
    #print('New height = %d' % height)
  else:
    count += 1
    #print('Piece placed!')
    #print('Hit bottom! Total pieces = %d' % count)
    cave = place_piece_in_cave(cave, piece_in_flight, height, left, '#')
    #print_cave(count)
    
    piece_in_flight += 1
    piece_in_flight %= len(pieces)
    height = len(cave) - 1
    while cave[height] == empty:
      height -= 1
    height += 4 
    left = 2
    while len(cave) <= height+pieces[piece_in_flight]['height']:
      cave.append(empty.copy())
    #print('New piece!')
    #disp = place_piece_in_cave(copy.deepcopy(cave), piece_in_flight, height, left, '@')
    #print_cave(disp)


#print_cave(cave)
h = len(cave)
while h >=0:
  h -= 1
  if cave[h] != empty:
    print('Height is %d' % h)
    break
