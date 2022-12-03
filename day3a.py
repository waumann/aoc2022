#!/usr/bin/python

file1 = open('input.day3.txt', 'r')
lines = file1.readlines()

score = dict()
for i in range(65, 91):
  score[chr(i)] = i - 64 + 26
for i in range(97, 123):
  score[chr(i)] = i - 96

prisum = 0
for line in lines:
  ll = int(len(line.strip()) / 2)
  a = set()
  for c in line[:ll]:
    a.add(c)
  b = set()
  for c in line[ll:]:
    b.add(c)
  oops = a.intersection(b)
  assert len(oops) == 1
  item = oops.pop()
  prisum += score[item] 

print('Total = %d' % prisum)
