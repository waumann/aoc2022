#!/usr/bin/python3

import sys

with open("input.day25.txt", "r") as f:
  all = f.readlines()
with open("s_to_d.txt", "r") as f:
  stest = f.readlines()
with open("d_to_s.txt", "r") as f:
  dtest = f.readlines()

values = {
  '2':  2,
  '1':  1,
  '0':  0,
  '-': -1,
  '=': -2,
}

def s_to_d(instr):
  val = 0
  place_val = 1
  for i in range(len(instr)-1, -1, -1):
    val += place_val * values[instr[i]]
    place_val *= 5
  return val

places = dict()
powers_of_5 = dict()
powers_of_5_times_2 = dict()
max_under = dict()

def init_dicts(sum):
  p = 0
  max_under[0] = 0
  while True:
    places[p] = pow(5, p)
    powers_of_5[places[p]] = p
    powers_of_5_times_2[places[p] * 2] = p
    if p > 0: max_under[p] = max_under[p-1] + 2 * places[p-1]
    print('%2d: %15d (%15d)' % (p, places[p], max_under[p]))
    if max_under[max(p-1, 0)] > sum: break
    p += 1

def p_of_5(x, i, ostr):  
    to_add = None
    k = None
    if x in powers_of_5:
      to_add = '1'
      k = powers_of_5[x]
    elif x in powers_of_5_times_2:
      to_add = '2'
      k = powers_of_5_times_2[x]
    elif abs(x) in powers_of_5:
      to_add = '-'
      k = powers_of_5[abs(x)]
    elif abs(x) in powers_of_5_times_2:
      to_add = '='
      k = powers_of_5_times_2[abs(x)]
    if not to_add: return None
    lead = i - k
    if len(ostr) > 0:
      for _ in range(lead): ostr += '0'
    ostr += to_add
    for _ in range(k): ostr += '0'
    return ostr

def d_to_s(sum):
  ostr = ''
  oval = 0
  digits = None
  for i in range(len(places)):
    if max_under[i] > sum:
      digits = i
      break
  print('Starting with %d' % sum)
  print('Working with %d digits' % digits)
  print('max_under range goes to %d' % len(max_under.keys()))
  print('Starting with %d, working with %d digits (max is %d)' % (sum, digits, max_under[digits]))
  for i in range(digits, -1, -1):
    remaining = sum - oval
    print('  Remaining = %d, working on %d place (%d)' % (remaining, i, places[i]))
    test_end = p_of_5(remaining, i, ostr)
    if test_end is not None:
      print('  Remaining is simple multiple of power of 5.')
      return test_end
    print('  Check remaining(abs(%d)) is within %d' % (remaining, max_under[i+1]))
    assert(abs(remaining) < max_under[i+1])
    print('  Checking abs(%d) with %d and %d' % (abs(remaining), places[i], max_under[i]))
    assert(abs(remaining) < max_under[i+1])
    if remaining > (places[i] + max_under[i]):
      print('Adding 2 because %d > %d' % (remaining, places[i] + 2 * places[i-1]))
      ostr += '2'
      oval += places[i] * 2
    elif remaining > max_under[i]:
      print('Adding 1 because %d > %d' % (remaining, places[i-1] * 2))
      ostr += '1'
      oval += places[i]
    elif remaining < -places[i] - max_under[i]: 
      print('Adding = because %d < %d' % (remaining, -(places[i] + 2 * places[i-1])))
      ostr += '='
      oval -= places[i] * 2
    elif remaining < -max_under[i]:
      print('Adding - because %d < %d' % (remaining, -(places[i-1] * 2)))
      ostr += '-'
      oval -= places[i]
    elif len(ostr) > 0:
      print('Adding 0')
      ostr += '0'
    else:
      print('Adding nothing')


sum = 0
for line in all:
  v = line.strip()
  d = s_to_d(v)
  sum += d

init_dicts(sum)

for l in stest:
  s, d = l.strip().split()
  assert(s_to_d(s) == int(d))

for l in dtest:
  d_s, s = l.strip().split()
  d = int(d_s)
  print('DEBUG: Testing %d' % d)
  d_conv = d_to_s(d)
  print('DEBUG: Convert %d to "%s" (should match "%s")' % (d, d_conv, s))
  assert(d_conv == s)


print('SNAFU is %s' % d_to_s(sum))
