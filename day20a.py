#!/usr/bin/python3

import sys

with open("input.day20.txt", "r") as f:
  all = f.readlines()

orig = []
out = []

for line in all:
  l = line.strip()
  orig.append(int(l))
  out.append(int(l))

length = len(orig)

def move_positive(input, value):
  work = input.copy()
  loc = input.index(value)
  offset = value % length
  if abs(value) > length: offset += 1
  if loc > 0:
    work = work[loc:] + work[:loc]
  assert(work[0] == value)
  return work[1:offset+1] + [value] + work[offset+1:]

def move_negative(input, value):
  work = input.copy()
  loc = input.index(value)
  offset = value % length
  if abs(value) > length: offset -= 1
  if loc < length - 1:
    work = work[loc+1:] + work[0:loc+1]
  assert(work[length-1] == value)
  return work[:offset-1] + [i] + work[offset-1:length-1]


count = 0
for i in orig:
  count += 1
  #print('Count = %d, value = %d' % (count, i))
  offset = i % len(out)
  loc = out.index(i)
  newloc = loc + offset % length 
  if i > 0:
    out = move_positive(out, i)
  elif i < 0:
    out = move_negative(out, i)
  else:
    pass

# print('Final = %s' % out)
start = out.index(0)
i1 = (start + 1000) % len(out)
print('i1 = %d + 1000 mod %d = %d' % (start, len(out), i1))
i2 = (start + 2000) % len(out)
print('i2 = %d + 2000 mod %d = %d' % (start, len(out), i2))
i3 = (start + 3000) % len(out)
print('i3 = %d + 3000 mod %d = %d' % (start, len(out), i3))
print('Coordinate = %d + %d + %d = %d' % (out[i1], out[i2], out[i3], out[i1] + out[i2] + out[i3]))

print('Not -13097')

