#!/usr/bin/python3

from math import ceil
from operator import add, sub
import re

with open("input.day19.txt", "r") as f:
  all = f.readlines()

ORE = 0
CLAY = 1
OBS = 2
GEODE = 3

TIME = 32

compounded = [None] * TIME

robot_name = {
  0: 'ore-collecting',
  1: 'clay-collecting',
  2: 'obsidian-collecting',
  3: 'geode-collecting'
}

resource_name = {
  0: 'ore',
  1: 'clay',
  2: 'obsidian',
  3: 'geode',
}

build_letter = {
  0: 'o',
  1: 'c',
  2: 'O',
  3: 'g',
}

compounded[0] = 0
robots = 0
resources = 0
for i in range(TIME):
  resources += robots
  robots += 1
  compounded[i] = resources
  

class Blueprint:
  def __init__(self, id, ore_robot, clay_robot, obs_robot_ore, obs_robot_clay, geode_robot_ore, geode_robot_obs):
    self.id = id
    self.building = None
    self.robot_costs = [
        [ore_robot, 0, 0, 0],                     ## ore
        [clay_robot, 0, 0, 0],                    ## clay
        [obs_robot_ore, obs_robot_clay, 0, 0],    ## obsidian
        [geode_robot_ore, 0, geode_robot_obs, 0], ## geode
    ]

    self.robot_limits = [
        max([ore_robot, clay_robot, obs_robot_ore, geode_robot_ore]),
        obs_robot_clay,
        geode_robot_obs,
        100
    ]

  def collect(self, resources, robots):
    return list(map(add, resources, robots))

  def purchase(self, rtype, resources):
    return list(map(sub, resources, self.robot_costs[rtype]))

  def cannot_purchase(self, rtype, robots):
    for r in range(4):
      if self.robot_costs[rtype][r] > 0 and robots[r] == 0: return True
    return False

  def time_needed(self, rtype, resources, robots):
    needed = 0
    for r in range(4):
      try:
        needed = max(needed, int(ceil((self.robot_costs[rtype][r] - resources[r]) / robots[r])))
      except ZeroDivisionError: pass
    return needed

  def run_plan(self, time_in, resources_in, robots_in, build_num, builds, best_so_far):
    best_so_far = max(resources_in[3], best_so_far)
    geodes_from_existing_robots = (TIME + 1 - time_in) * robots_in[3]
    #if geodes_from_existing_robots + compounded[TIME - time_in] < best_so_far:
    #  return geodes
    for rtype in range(3, -1, -1):
      robots = robots_in.copy()
      resources = resources_in.copy()
      time_t = time_in
      # Don't build a new one if we don't need it
      if robots[rtype] >= self.robot_limits[rtype]:
        continue
      if self.cannot_purchase(rtype, robots):
        continue
      time_needed = self.time_needed(rtype, resources, robots)
      # Fast forward by time_needed, plus one to do the build
      if time_t + time_needed + 1 > TIME:
        if robots[3] == 0:
          continue
        while time_t < TIME + 1:
          resources = self.collect(resources, robots)
          time_t += 1
        best_so_far = max(best_so_far, resources[3])
        continue
      for tt in range(time_needed):
        resources = self.collect(resources, robots)
      time_t += time_needed
      resources = self.purchase(rtype, resources)
      resources = self.collect(resources, robots)
      robots[rtype] += 1
      geodes = self.run_plan(time_t + 1, resources, robots, build_num + 1, builds + build_letter[rtype], best_so_far)
      best_so_far = max(best_so_far, geodes)
    return best_so_far


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

product = 1
for plan in plans:
  plan_id = plan.id
  if plan_id > 3: break
  best = plan.run_plan(1, [0, 0, 0, 0], [1, 0, 0, 0], 1, '', 0)
  print('Plan %d best = %d' % (plan_id, best))
  product *= best

print('Product is %d' % product)
