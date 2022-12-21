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
  '=': eq,
}

def get_int(ptr):
  a, b = vars[ptr]
  va = vars[a]
  vb = vars[b]
  rtnptr = None
  if isinstance(va, int): return (va, b)
  elif isinstance(vb, int): return (vb, a)
  else:
    print('Neither side of "%s" has a value!' % ptr)
    sys.exit(0)


def get_right_int(ptr):
  a, b = vars[ptr]
  vb = vars[b]
  rtnptr = None
  if isinstance(vb, int): return (vb, a)
  else: return None, None


def get_left_int(ptr):
  a, b = vars[ptr]
  va = vars[a]
  if isinstance(va, int): return (va, b)
  else: return None, None


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
    
vars['humn'] = None
ops['root'] = '='

while True:
  changed = 0
  worklist = [k for k in ops.keys()]
  print('Worklist has %d items' % len(worklist))
  for k in worklist:
    a, b = vars[k]
    if isinstance(vars[a], int) and isinstance(vars[b], int):
      vars[k] = fref[ops[k]](vars[a], vars[b])
      del ops[k]
      changed += 1
  if changed == 0: break

curr = 'root'
needed = 0
while True:
  print('Starting with "%s", needed = %d' % (curr, needed))
  if curr == 'humn':
    print('Value needed is %d' % needed)
    sys.exit(0)
  lptr, rptr = vars[curr]
  lv = vars[lptr]
  rv = vars[rptr]
  print('Operation is "%s"' % ops[curr])
  if ops[curr] == '=':
    if isinstance(lv, int): 
      needed = lv
      curr = rptr
    elif isinstance(rv, int): 
      needed = rv
      curr = lptr
    else:
      print('Neither side has a value!')
      sys.exit(0)
  elif ops[curr] == '+':
    num, ptr = get_int(curr)
    needed -= num
    curr = ptr
  elif ops[curr] == '*':
    num, ptr = get_int(curr)
    needed /= num
    curr = ptr
  elif ops[curr] == '-':
    num, ptr = get_right_int(curr)
    if num is not None:
      needed += num
      curr = ptr
    else:
      num, ptr = get_left_int(curr)
      if num is None:
        print('Neither side of "%s" has a value!' % curr)
        sys.exit(0)
      needed = num - needed
      curr = ptr
  elif ops[curr] == '/':
    num, ptr = get_right_int(curr)
    if num is not None:
      needed *= num
      curr = ptr
    else:
      num, ptr = get_left_int(curr)
      if num is None:
        print('Neither side of "%s" has a value!' % curr)
        sys.exit(0)
      needed = num / needed
      curr = ptr
