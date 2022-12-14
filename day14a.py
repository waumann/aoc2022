#!/usr/bin/python3

with open("input.day14.txt", "r") as f:
  all = f.readlines()

mymap = dict()

min_x = 500
max_x = 500
max_y = 0
for line in all:
  lx = None
  ly = None
  l = line.strip()
  points = l.split(' -> ')
  for point in points:
    sx, sy = point.split(',')
    x = int(sx)
    y = int(sy)
    min_x = min(x, min_x)
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    if lx or ly:
      print("Loop: lx: %d, ly: %d, x: %d, y: %d" % (lx, ly, x, y))
      if lx == x:
        for i in range(min([ly, y]), max([ly, y]) + 1):
          mymap.setdefault(x, dict())
          mymap[x][i] = "#"
      else:
        assert(ly == y)
        for i in range(min([lx, x]), max([lx, x]) + 1):
          mymap.setdefault(i, dict())
          mymap[i][y] = "#"
    lx = x
    ly = y

max_x += 2
min_x -= 1
max_y += 2

for y in range(0, max_y+1):
  for x in range(min_x, max_x):
    mymap.setdefault(x, dict())
    mymap[x].setdefault(y, ".")
    print(mymap[x][y], end="")
  print()
print()

def add_sand(x, y):
  global mymap
  while True: 
    if y >= max_y:
      break
    if mymap[x][y+1] != "." and mymap[x-1][y+1] != "." and mymap[x+1][y+1] != ".":
      break
    
    if mymap[x][y+1] == ".":
      y = y + 1
      continue

    if mymap[x-1][y+1] == ".":
      x = x - 1
      y = y + 1
      continue

    if mymap[x+1][y+1] == ".":
      x = x + 1
      y = y + 1
      continue

  if y >= max_y:
    return False

  mymap[x][y] = "o"
  return True

added = 0
while add_sand(500, 0):
  added += 1

print("Added %d sand" % added)

