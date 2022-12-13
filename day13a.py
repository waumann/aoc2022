#!/usr/bin/python3

import os

### NOT 5035
### NOT 5065

with open("input.day13.txt", "r") as f:
  all = f.readlines()

def do_eval(a, b):
  print("Compare %s vs %s" % (a, b))
  if isinstance(a, int) and isinstance(b, int):
    if a < b: 
      print("Left side is smaller, so inputs are in the right order")
      return -1
    if a > b:
      print("Right side is smaller, so inputs are not in the right order")
      return 1
    if a == b: return 0
  if isinstance(a, int) and isinstance(b, list):
    print("Mixed types; convert left to [%d] and retry comparison" % a)
    return do_eval([a], b)
  if isinstance(a, list) and isinstance(b, int):
    print("Mixed types; convert right to [%d] and retry comparison" % b)
    return do_eval(a, [b])
  if isinstance(a, list) and isinstance(b, list):
    index = 0
    while True:
      if index >= len(a) and index < len(b):
        print("Left side ran out of items, so inputs are in the right order")
        return -1
      if index < len(a) and index >= len(b):
        print("Right side ran out of items, so inputs are not in the right order")
        return 1
      if index >= len(a) and index >= len(b): return 0
      recurse = do_eval(a[index], b[index])
      if recurse != 0: return recurse
      index += 1 
      

index = 1
sum = 0

print("Length = %d" % len(all))

while True:
  if 3*(index - 1) > len(all): break
  left = eval(all[3*(index-1)])
  right = eval(all[3*(index-1)+1])
  print("== Pair %d ==" % index)
  #print("Left:: %s" % left)
  #print("Right: %s" % right)

  if do_eval(left, right) == -1:
    print("In Order")
    sum += index
  else:
    print("Out of Order")
  index += 1
  print("")

print("Sum = %d" % sum)
