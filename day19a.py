#!/usr/bin/python3

from enum import Enum
import sys
import re
import copy

with open("input.day19.test", "r") as f:
  all = f.readlines()

ORE = 0
CLAY = 1
OBS = 2
GEODE = 3

robot_name = {
  0: 'ore-collecting',
  1: 'clay-collecting',
  2: 'obsidian-collecting',
  3: 'geode-collecting'
}

class Robot:
  def __init__(self, mines, ore_cost, clay_cost, obs_cost):
    self.mines = mines
    self.ore_cost = ore_cost
    self.clay_cost = clay_cost
    self.obs_cost = obs_cost

  def build(self, node):
    desc = robot_name[self.mines]
    #print('Checking for %s:' % desc)
    #print('Cost = %d, Ore = %d' % (self.ore_cost, node.ore))
    if node.ore < self.ore_cost or node.clay < self.clay_cost or node.obs < self.obs_cost: return None

    #print('Building!')
    rtn = copy.deepcopy(node)
    desc = robot_name[self.mines]
    msg = 'Spent %d ore ' % self.ore_cost
    if self.clay_cost:
      msg += 'and %d clay ' % self.clay_cost
    if self.obs_cost:
      msg += 'and %d obsidian ' % self.obs_cost
    msg += 'to start building one %s.' % desc
    rtn.log.append(msg)
    rtn.ore -= self.ore_cost
    rtn.clay -= self.clay_cost
    rtn.obs -= self.obs_cost
    rtn.building = self.mines
    return rtn

class Blueprint:
  def __init__(self, id, ore_robot, clay_robot, obs_robot_ore, obs_robot_clay, geode_robot_ore, geode_robot_obs):
    self.id = id
    self.building = None
    self.ore_robot = Robot(ORE, ore_robot, 0, 0)
    self.clay_robot = Robot(CLAY, clay_robot, 0, 0)
    self.obs_robot = Robot(OBS, obs_robot_ore, obs_robot_clay, 0)
    self.geode_robot = Robot(GEODE, geode_robot_ore, 0, geode_robot_obs)
    self.log = []

    self.time_r = 1

    self.ore_robots = 1
    self.clay_robots = 0
    self.obs_robots = 0
    self.geode_robots = 0

    self.ore = 0
    self.clay = 0
    self.obs = 0
    self.geodes = 0

  def print(self):
    build = 'Nothing'
    if self.building is not None:
      build = robot_type[self.building]
    print('T=%d, ore=%d, clay=%d, bulidind %s' % (self.time_r, self.ore, self.clay, build))

  def collect(self):
    self.ore += self.ore_robots
    self.clay += self.clay_robots
    self.obs += self.obs_robots
    self.geodes += self.geode_robots

    if self.ore_robots > 0:
      self.log.append('%d ore-collecting robots collect %d ore; you now have %d ore.' % (self.ore_robots, self.ore_robots, self.ore))
    if self.clay_robots > 0:
      self.log.append('%d clay-collecting robots collect %d clay; you now have %d clay.' % (self.clay_robots, self.clay_robots, self.clay))
    if self.obs_robots > 0:
      self.log.append('%d obsidian-collecting robots collect %d obsidian; you now have %d obsidian.' % (self.obs_robots, self.obs_robots, self.obs))
    if self.geode_robots > 0:
      self.log.append('%d geode-collecting robots collect %d geodes; you now have %d geodes.' % (self.geode_robots, self.geode_robots, self.geodes))
      print('\n'.join(self.log))
      sys.exit(0)

  def finish_build(self):
    if not self.building: return
    desc = robot_name[self.building]
    count = None
    if self.building == ORE:
      self.ore_robots += 1
      count = self.ore_robots
    elif self.building == CLAY:
      self.clay_robots += 1
      count = self.clay_robots
    elif self.building == OBS:
      self.obs_robots += 1
      count = self.obs_robots
    elif self.building == GEODE:
      self.geode_robots += 1
      count = self.geode_robots

    self.log.append('The new %s robot is ready; you now have %d of them.' % (desc, count))
    self.building = None
      

  def run_plan(self):
    global geode_time
    print('== Minute %d ==' % self.time_r)
    self.log.append('== Minute %d ==' % self.time_r)
    if self.time_r == 24:
      self.collect()
      self.time_r = 25
      return self
    if self.time_r >= geode_time + 1 and self.geode_robots == 0:
      #print('Got node at t=%d, with geode robots after %d.' % (self.time_r, geode_time))
      self.time_r = 25
      return self
    if self.geode_robots > 0:
      print('\n'.join(self.log))
      sys.exit(0)

    #print('DEBUG: t=%d, ore=%d' % (self.time_r, self.ore))
    self.time_r = self.time_r + 1

    rtnlist = [self]
    node = self.geode_robot.build(self)
    if node: rtnlist.append(node)
    node = self.obs_robot.build(self)
    if node: rtnlist.append(node)
    node = self.clay_robot.build(self)
    if node:
      print('Adding clay robot node')
      rtnlist.append(node)
    node = self.ore_robot.build(self)
    if node:
      #print('Adding ore robot node')
      rtnlist.append(node)
    if len(rtnlist) > 1:
    print('

    for node in rtnlist:
      node.collect()
      node.finish_build()

    return rtnlist


  def get_time(self):
    return self.time_r


plans = []

for line in all:
  l = line.strip()
  m = re.search('Blueprint (\d*): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', l)
  plan_id = int(m.group(1))
  ore_robot = int(m.group(2))
  clay_robot = int(m.group(3))
  obs_robot_ore = int(m.group(4))
  obs_robot_clay = int(m.group(5))
  geode_robot_ore = int(m.group(6))
  geode_robot_obs = int(m.group(7))

  plan = Blueprint(plan_id, ore_robot, clay_robot, obs_robot_ore, obs_robot_clay, geode_robot_ore, geode_robot_obs)
  plans.append(plan)

print('Total plans = %d' % len(plans))

quality = 0
for plan in plans:
  plan_id = plan.id
  best = 0
  geode_time = 24
  workq = [plan]
  while len(workq) > 0:
    next_t = workq.pop(0)
    rtnval = next_t.run_plan()
    if isinstance(rtnval, int):
      pass
    elif isinstance(rtnval, list):
      workq.extend(rtnval)
    else:
      if rtnval.time_r == 25:
        if rtnval.geodes > best: best = rtnval.geodes
  print('Plan %d best = %d' % (plan_id, best))
  quality += best * plan_id

print('Total quality is %d' % quality)
