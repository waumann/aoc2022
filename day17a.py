#!/usr/bin/python3

with open("input.day17.test", "r") as f:
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

empty = '       '
assert(len(all) == 1)
input = all[0]
wind = 0
cave = ['#######', empty, empty, empty, empty]
piece_in_flight = 1
height = 4
left = 2

def check_left_collision(cave, piece_id, ht, left):

while piece_in_flight < 3:
  wind_dir = input[wind]
  if wind_dir == '<':
    test_left = max(0, left - 1)
    if not check_left_collision(cave, piece_in_flight, height, test_left):
      left = test_left
  else:
    test_left = min(left + 1, 7 - pieces[piece_in_flight]["width"]
    if not check_right_collision(cave, piece_in_flight, height, test_left):
      left = test_left





  bottom = pieces[piece_in_flight]["text"][0]  
  #for i in range(0, len(bottom)):
  #  if  

