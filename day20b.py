#!/usr/bin/python3

import sys

MULT = 811589153
ROUNDS = 10
# MULT, ROUNDS = 1, 1

out = [int(x) * MULT for x in open('input.day20.txt')]
order = list(range(len(out)))

length = len(out) - 1

def move(input, idx):
  loc = input.index(idx)
  ptr = input.pop(loc)
  raw_position = loc + out[idx]
  net_position = raw_position % length
  #print('Moving value by %d (was %d)' % (net_position, raw_position))
  #print('======================')
  input.insert(net_position, ptr)
  return input

for r in range(ROUNDS):
  print('Round %d' % r)
  for i in range(len(order)):
    #if r == 1: print('%3d: Moving %d' % (i, order[i]))
    order = move(order, i)
    #if r < 1: continue
    #if i < 6: continue
    #pos = out.index(0)
    #out = out[pos:] + out[:pos]
    #for x in out: print(x)
    #sys.exit(0)

# print('Final = %s' % out)
start = order.index(out.index(0))
print('Sum is %d' % sum(out[order[(start + offset) % len(order)]] for offset in [1000, 2000, 3000]))


#print('Not -15593062415802')
#print('Not 5871847521955')
#print('Not 5968426631162, too high')
