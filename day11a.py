#!/usr/bin/python3

import os

with open("input.day11.txt", "r") as f:
  all = f.readlines()

monkeys = []

class Monkey:
  def __init__(self, id, items, operation, divisor, iftrue, iffalse):
    self.id = id
    self.items = items
    self.divisor = int(divisor)
    self.iftrue = int(iftrue)
    self.iffalse = int(iffalse)
    self.count = 0
    number = operation.split(' ')[-1]
    if '+' in operation:
      self.operation = '+'
    elif '*' in operation:
      self.operation = '*'
    else:
      self.operation = '^'
    self.number = int(number)

  def throw(self):
    global monkeys
    for item in self.items:
      self.count += 1
      #print('Monkey inspects an item with a worry level of %d' % item)
      if self.operation == '+':
        worry = item + self.number
      elif self.operation == '*':
        worry = item * self.number
      else:
        worry = item * item
      #print('Worry level set to %d' % worry) 
      new = worry // 3
      #print('Monkey gets bored with item. Worry level drops to %d' % new)
      if new % self.divisor > 0:
        #print('Item thrown to monkey %d' % self.iffalse)
        monkeys[self.iffalse].catch(new)
      else:
        #print('Item thrown to monkey %d' % self.iftrue)
        monkeys[self.iftrue].catch(new)
    self.items = []

  def catch(self, worry):
    self.items.append(worry)

  def list(self):
    return ', '.join([str(x) for x in self.items])


id = 0
operation = ""
items = []
divisor = 0
iftrue = 0
iffalse = 0
for line in all:
  l = line.strip()
  if l.startswith('Monkey'):
    id = int(l[7])
  elif l.startswith('Starting items'):
    items = [int(x) for x in l[16:].split(', ')]
  elif l.startswith('Operation'):  
    operation = l[17:]
    if 'old * old' in operation:
      operation = '^ 2'
  elif l.startswith('Test'):  
    divisor_list = l.split(' ')
    divisor = int(divisor_list[-1])
  elif l.startswith('If true'):  
    iftrue = int(l[-1])
  elif l.startswith('If false'):  
    iffalse = int(l[-1])
  else:
    monkeys.append(Monkey(id, items, operation, divisor, iftrue, iffalse))
monkeys.append(Monkey(id, items, operation, divisor, iftrue, iffalse))

index = 0
round_num = 1
while True:
  #print('Index = %d' % index)
  m = monkeys[index]
  m.throw()

  index += 1
  if index == len(monkeys):
    #print('After round_num %d, the monkeys are holding items with these worry levels:' % round_num)
    #for i in range(0, index):
    #  print('Monkey %d: %s' % (i, monkeys[i].list()))
    round_num += 1
    index = 0
    if round_num == 21:
      break


vals = []
for i in range(0, len(monkeys)):
  print('Monkey %d inspected items %d times.' % (i, monkeys[i].count))
  vals.append(monkeys[i].count)

v = sorted(vals)
print('Level = %d' % (v[-1] * v[-2]))
