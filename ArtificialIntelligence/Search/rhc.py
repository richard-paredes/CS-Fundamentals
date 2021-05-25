import random


num_sol_searched = 0
def clamp(x, min_value, max_value):
  return max(min(x, max_value), min_value)


def objective_func(vector):
  global num_sol_searched
  num_sol_searched += 1

  x = vector[0]
  y = vector[1]
  return (1 + (x+y+1)**2 * (19-14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2))*(30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 4*y - 36*x*y + 27*y**2))


def get_neighbor(z, curr):
  while True:
    deltaX = random.uniform(-1*z, z)
    deltaY = random.uniform(-1*z, z)
    x = curr[0]+deltaX
    y = curr[1]+deltaY
    if x > 2 or x < -2 or y > 2 or y < -2:
      continue
    return (x, y)


def RHC(sp, p, z, seed=random.random()):
  random.seed(seed)
  z = abs(z)
  num_sol_searched = [0]
  local_min = sp
  while True:
    current_min = local_min
    neighbors = [current_min]
    for i in range(p):
      neighbor_sol = get_neighbor(z, current_min)
      neighbors.append(neighbor_sol)
    current_min = min(neighbors, key=lambda sol: objective_func(sol))
    # print(local_min, current_min, objective_func(local_min) == objective_func(current_min))
    if (local_min == current_min):
      break
    local_min = current_min

  return local_min


def main():
  count = 0
  global num_sol_searched
  for seed in [1, 2]:
    for sp in [(0.4, -0.5), (-0.5, 0.3), (1, -2), (0, 0)]:
      for p in [30, 120]:
        for z in [0.03, 0.1]:
          num_sol_searched = 0
          count += 1
          sol = RHC(sp, p, z, seed)
          print(f"{count}. Starting values: {sp}, {p}, {z}, {seed}")
          print(f"Solution: {sol}")
          print(f"# Solutions Searched: {num_sol_searched}")
          print(f"Initial objective: {objective_func(sp)}")
          print(f"Final Objective: {objective_func(sol)}")
          print()
    
  # 33rd run
  sp = [2, 2]
  p = 1000
  z = 0.25
  num_sol_searched = 0
  sol = RHC(sp, p, z, seed)
  print(f"{33}. Starting values: {sp}, {p}, {z}, {seed}")
  print(f"Solution: {sol}")
  print(f"# Solutions Searched: {num_sol_searched}")
  print(f"Initial objective: {objective_func(sp)}")
  print(f"Final Objective: {objective_func(sol)}")
  print()


main()
