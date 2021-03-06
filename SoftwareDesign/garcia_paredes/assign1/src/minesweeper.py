from enum import Enum
from random import Random
from itertools import product

class CellState(Enum):
  UNEXPOSED = 0
  EXPOSED = 1
  SEALED = 2

class GameStatus(Enum):
  INPROGRESS = 0
  LOST = 1
  WON = 2

class Minesweeper:
  SIZE = 10
  NUM_MINES = 10

  def __init__(self):
    self.cell_states = [[CellState.UNEXPOSED for i in range(self.SIZE)] for j in range(self.SIZE)]
    self.mined_cells = [[False for i in range(self.SIZE)] for j in range(self.SIZE)]

  def get_cell_status(self, x: int, y: int):
    return self.cell_states[x][y]

  def expose_cell(self, x: int, y: int):
    if self.get_cell_status(x, y) == CellState.UNEXPOSED:
      self.cell_states[x][y] = CellState.EXPOSED

      if self.adjacent_mines_count_at(x, y) == 0:
        self.expose_neighbors(x, y)

  def toggle_seal(self, x: int, y: int):
    self.cell_states[x][y] = {
        CellState.UNEXPOSED: CellState.SEALED,
        CellState.SEALED: CellState.UNEXPOSED,
        CellState.EXPOSED: CellState.EXPOSED
    }[self.get_cell_status(x, y)]

  def expose_neighbors(self, x: int, y: int):
    start_x = max(0, x - 1)
    end_x = min(self.SIZE, x + 2)

    start_y = max(0, y - 1)
    end_y = min(self.SIZE, y + 2)

    for i, j in product(range(start_x, end_x), range(start_y, end_y)):
        self.expose_cell(i, j)

  def is_mine_at(self, x: int, y: int):
    return not any(val not in range(0, self.SIZE) for val in [x, y]) and self.mined_cells[x][y]

  def adjacent_mines_count_at(self, x: int, y: int):
    start_x = max(0, x - 1)
    end_x = min(self.SIZE, x + 2)

    start_y = max(0, y - 1)
    end_y = min(self.SIZE, y + 2)

    mine_count = 0

    for i, j in product(range(start_x, end_x), range(start_y, end_y)):
      mine_count += self.is_mine_at(i, j)

    return mine_count - 1 if self.is_mine_at(x, y) else mine_count

  def get_game_status(self):
    game_status = GameStatus.WON
    for i, j in product(range(self.SIZE), range(self.SIZE)):
      cell_state = self.get_cell_status(i, j)
      is_mine = self.is_mine_at(i, j)
      if is_mine:
        if cell_state == CellState.EXPOSED:
          game_status = GameStatus.LOST
          break
      elif cell_state != CellState.EXPOSED:
        game_status = GameStatus.INPROGRESS

    return game_status

  def set_mines(self, seed: int):
    random = Random(seed)
    num_mined_cells = 0

    while num_mined_cells < self.NUM_MINES:
      x = random.randint(0, self.SIZE - 1)
      y = random.randint(0, self.SIZE - 1)
      num_mined_cells += not self.is_mine_at(x, y)
      self.mined_cells[x][y] = True
