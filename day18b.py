#!/usr/bin/python3

import sys

sys.setrecursionlimit(5000)

with open("input.day18.txt", "r") as f:
  all = f.readlines()

cubes = set()

faces = 0

x = None
y = None
z = None

def is_inside(trial, x, y, z):
  global min_x
  global min_y
  global min_z
  global max_x
  global max_y
  global max_z

  key = (x, y, z)
  if key in cubes: return False
  if x == min_x or x == max_x or y == min_y or y == max_y or z == min_z or z == max_z: return False 
  trial.add((x, y, z))
  for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
    tx = x + dx
    ty = y + dy
    tz = z + dz
    testkey = (tx, ty, tz)
    if testkey in cubes:
      continue
    if testkey in trial:
      continue
    if is_inside(trial, tx, ty, tz) == False:
      return False
  return True

def deal_with_inside(sx, sy, sz):
  global cubes
  key = (sx, sy, sz)
  pocket = {key}
  added = 1
  ## print('Starting with (%d, %d, %d)' % key)
  to_add = set()
  while added > 0:
    ## print('Starting pocket loop')
    added = 0
    for key in pocket:
      x, y, z = key
      ## print('Starting delta loop for (%d, %d, %d)' % key)
      for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        tx = x + dx
        ty = y + dy
        tz = z + dz
        testkey = (tx, ty, tz)
        if testkey in cubes:
          ## print('(%d, %d, %d) in cubes' % testkey)
          continue
        if testkey in pocket:
          ## print('(%d, %d, %d) already in pocket' % testkey)
          continue
        added += 1
        ## print('Adding (%d, %d, %d) to pocket' % testkey)
        to_add.add(testkey)
    pocket.update(to_add)
    to_add.clear()
  internal_faces = 0
  for point in pocket:
    print('Pocket point: (%d, %d, %d)' % point)
    x, y, z = point
    internal_faces += 6
    for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
      testkey = (x+dx, y+dy, z+dz)
      if testkey in pocket:
        print('Found (%d, %d, %d) in pocket' % testkey)
        internal_faces -= 1
    cubes.add(point)
  return internal_faces

for line in all:
  l = line.strip()
  sx, sy, sz = l.split(',')
  x = int(sx)
  y = int(sy)
  z = int(sz)
  faces += 6
  for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
    testkey = (x+dx, y+dy, z+dz)
    if testkey in cubes:
      faces -= 2
  cubes.add((x, y, z))
print('Initial faces = %d' % faces)

min_x = max_x = x
min_y = max_y = y
min_z = max_z = z

for (x, y, z) in cubes:
  if x < min_x: min_x = x
  if y < min_y: min_y = y
  if z < min_z: min_z = z
  if x > max_x: max_x = x
  if y > max_y: max_y = y
  if z > max_z: max_z = z

print('x: %d - %d, y: %d - %d, z: %d - %d' % (min_x, max_x, min_y, max_y, min_z, max_z))

for x in range(min_x+1, max_x):
  for y in range(min_y+1, max_y):
    for z in range(min_z+1, max_z):
      trial = set()
      if is_inside(trial, x, y, z):
        ## print('(%d, %d, %d) is inside' % (x, y, z))
        delta = deal_with_inside(x, y, z)
        print('Removing %d faces' % delta)
        faces -= delta

print('Faces = %d' % faces)
