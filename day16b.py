#!/usr/bin/python3

import sys
import re
import itertools
import easygraph as eg

with open("input.day16.txt", "r") as f:
  all = f.readlines()

paths = dict()
rates = dict()

for line in all:
  l = line.strip()
  m = re.search('Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? (.*)', l)
  valve = m.group(1)
  flow = int(m.group(2))
  tunnels = m.group(3).split(', ')
  rates[valve] = flow
  paths[valve] = tunnels

graph = eg.Graph()
for k in paths.keys():
  graph.add_node(k)

for k in paths.keys():
  for d in paths[k]:
    if k < d: graph.add_edge(k, d)

max_rate = sorted(rates.values())[-1]
to_visit_unsorted = [x for x in rates.keys() if rates[x] > 0]
to_visit = sorted(to_visit_unsorted, key=lambda x:max_rate-rates[x])
print("Ordered = %s" % to_visit)
all_needed = to_visit.copy()
all_needed.append('AA')

cost = dict()
for x in all_needed:
  cost.setdefault(x, dict())
  out = eg.functions.path.Dijkstra(graph, x)
  for y in to_visit:
    cost[x][y] = out[y]

stops = set(to_visit)

def add_in_all_positions(input, node):
  rtnlist = []
  for pos in range(1, len(input)):
    n = input.copy()
    n.insert(pos, node)
    rtnlist.append(n)
  input.append(node)
  rtnlist.append(input)
  return rtnlist

def score(valves):
  global rates
  rtn = 0
  for v, t in valves.items():
    rtn += rates[v] * t
  return rtn


def explore(valves, remaining, hnode, enode, h_t, e_t):
  yield valves
  global cost

  if h_t < 2:
    for v in remaining:
      new_t = e_t - cost[enode][v] - 1
      if new_t < 2: continue
      new_remaining = remaining.copy()
      new_remaining.discard(v)
      new_valves = valves.copy()
      new_valves[v] = new_t
      yield from explore(new_valves, new_remaining, hnode, v, h_t, new_t)
  else:
    for v in remaining:
      new_t = h_t - cost[hnode][v] - 1
      if new_t < 2: 
        yield from explore(valves, remaining, hnode, enode, new_t, e_t)

      new_remaining = remaining.copy()
      new_remaining.discard(v)
      new_valves = valves.copy()
      new_valves[v] = new_t
      yield from explore(new_valves, new_remaining, v, enode, new_t, e_t)

max = 0
for path in explore({}, stops, 'AA', 'AA', 26, 26):
  val = score(path)
  if val > max:
    max = val

print('Score is %d' % max)
