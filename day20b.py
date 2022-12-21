#!/usr/bin/python3

import sys

with open("input.day20.test", "r") as f:
  all = f.readlines()

orig = []
out = []

for line in all:
  l = int(line.strip()) * 811589153
  orig.append(l)
  out.append(l)

length = len(orig) - 1

def move_positive(input, value):
  work = input.copy()
  loc = input.index(value)
  offset = value % length
  if loc > 0:
    work = work[loc:] + work[:loc]
  assert(work[0] == value)
  return work[1:offset+1] + [value] + work[offset+1:]

def move_negative(input, value):
  work = input.copy()
  loc = input.index(value)
  offset = value % length
  if loc < length:
    work = work[loc+1:] + work[0:loc+1]
  assert(work[length] == value)
  return work[:offset-1] + [i] + work[offset-1:length]


for count in range(0, 10):
  for i in orig:
    offset = i % len(out)
    if i > 0:
      out = move_positive(out, i)
    elif i < 0:
      out = move_negative(out, i)
    else:
      pass
    oo = out.copy()
  front = oo.index(0)
  print('XRound %d: %s' % (count, oo[front:] + oo[:front]))

# print('Final = %s' % out)
start = out.index(0)
i1 = (start + 1000) % len(out)
print('i1 = %d + 1000 mod %d = %d' % (start, len(out), i1))
i2 = (start + 2000) % len(out)
print('i2 = %d + 2000 mod %d = %d' % (start, len(out), i2))
i3 = (start + 3000) % len(out)
print('i3 = %d + 3000 mod %d = %d' % (start, len(out), i3))
print('Coordinate = %d + %d + %d = %d' % (out[i1], out[i2], out[i3], out[i1] + out[i2] + out[i3]))

print('Not -15593062415802')
print('Not 5871847521955')
