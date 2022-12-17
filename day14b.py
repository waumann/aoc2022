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

mymap[500][0] = "+"

max_x += 2
min_x -= 1
max_y += 2

def print_map():
  for y in range(0, max_y+1):
    for x in range(min_x, max_x+1):
      mymap.setdefault(x, dict())
      mymap[x].setdefault(y, ".")
      #print(mymap[x][y], end="")
  #  print()
  #print()

#print_map()

def add_sand(x, y):
  global mymap
  global min_x
  global max_x
  global max_y

  while True: 
    if x-1 < min_x:
       #print("Pushing border left")
       min_x = x-1
    if x+1 > max_x:
       #print("Pushing border right")
       max_x = x+1
    mymap.setdefault(x-1, dict())
    mymap[x-1][max_y] = "#"
    mymap.setdefault(x+1, dict())
    mymap[x+1][max_y] = "#"

    for i in range(x-1, x+2):
      mymap[i].setdefault(y+1, ".")
    #print("DEBUG: min_x = %d, max_x = %d, max_y = %d" % (min_x, max_x, max_y))
    #print("DEBUG: x = %d, y = %d" % (x, y))

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

  if x == 500 and y == 0:
    return False
  mymap[x][y] = "o"
  return True

added = 0
while add_sand(500, 0):
  added += 1
added += 1

print("Added %d sand" % added)

