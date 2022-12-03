#!/usr/bin/python

file1 = open('input.day3.txt', 'r')
lines = file1.readlines()

score = dict()
for i in range(65, 91):
  score[chr(i)] = i - 64 + 26
for i in range(97, 123):
  score[chr(i)] = i - 96

prisum = 0

lineptr = 0
while (True):
  x = set()
  for c in lines[lineptr].strip():
    x.add(c)
  y = set()
  for c in lines[lineptr + 1].strip():
    y.add(c)
  z = set()
  for c in lines[lineptr + 2].strip():
    z.add(c)
  maybe = x.intersection(y)
  badge = z.intersection(maybe)
  assert len(badge) == 1
  item = badge.pop()
  prisum += score[item] 
  lineptr += 3
  if lineptr >= len(lines):
    break

print('Total = %d' % prisum)
