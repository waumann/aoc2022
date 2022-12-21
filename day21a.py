#!/usr/bin/python3

import re
import sys

with open("input.day21.txt", "r") as f:
  all = f.readlines()

vars = dict()
ops = dict()

def add(a, b): return a+b
def sub(a, b): return a-b
def mul(a, b): return a*b
def div(a, b): return int(a/b)
def eq(a, b): return a == b

fref = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': div,
}

for line in all:
  l = line.strip()
  try:
    m = re.search('(\w+): (\d+)', l)
    vars[m.group(1)] = int(m.group(2))
  except:
    m = re.search('(\w+): (\w+) (.) (\w+)', l)
    name = m.group(1)
    var1 = m.group(2)
    var2 = m.group(4)
    vars[name] = (var1, var2)
    ops[name] = m.group(3)
    
while True:
  changed = 0
  worklist = [k for k in ops.keys()]
  print('Worklist has %d items' % len(worklist))
  for k in worklist:
    a, b = vars[k]
    if not isinstance(vars[a], tuple) and not isinstance(vars[b], tuple):
      vars[k] = fref[ops[k]](vars[a], vars[b])
      del ops[k]
      if k == 'root':
        print('Answer is %d' % vars[k])
        sys.exit(0)
