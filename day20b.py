#!/usr/bin/python3

import sys

out = [int(x) * 811589153 for x in open('input.day20.test')]
order = out.copy()

length = len(out)

def move(input, value):
  if value == 0: return input
  work = input.copy()
  loc = input.index(value)
  keep = work.pop(loc)
  work.insert((loc + keep) % length, keep)
  return work

print(out)

for _ in range(10):
  for i in order:
    out = move(out, i)
    #pos = out.index(0)
    #out = out[pos:] + out[:pos]
    #for x in out: print(x)
    #print('============')
  #sys.exit(0)

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
print('Not 5968426631162 is too high')
