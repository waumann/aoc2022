#!/usr/bin/python3


with open("input.day18.txt", "r") as f:
  all = f.readlines()

cubes = set()

faces = 0

for line in all:
  l = line.strip()
  sx, sy, sz = l.split(',')
  x = int(sx)
  y = int(sy)
  z = int(sz)
  faces += 6
  for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
    testkey = '%d:%d:%d' % (x+dx, y+dy, z+dz)
    if testkey in cubes:
      faces -= 2
  cubes.add('%d:%d:%d' % (x, y, z))
print('Total faces = %d' % faces)
