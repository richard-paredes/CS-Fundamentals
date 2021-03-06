from unittest import main, TestCase, mock
from unittest.mock import call

from minesweeper import Minesweeper, CellState, GameStatus

class MinesweeperTests(TestCase):
  def setUp(self):
    self.minesweeper = Minesweeper()

  def test_Canary(self):
    self.assertTrue(True)

  def test_initial_cell_state_is_unexposed(self):
    self.assertEqual(CellState.UNEXPOSED, self.minesweeper.get_cell_status(0, 0))

  def test_expose_an_unexposed_cell_exposes_cell(self):
    self.minesweeper.expose_cell(0, 0)

    self.assertEqual(CellState.EXPOSED, self.minesweeper.get_cell_status(0, 0))

  def test_expose_an_exposed_cell_exposes_cell(self):
    self.minesweeper.expose_cell(1, 1)

    self.minesweeper.expose_cell(1, 1)

    self.assertEqual(CellState.EXPOSED, self.minesweeper.get_cell_status(1, 1))

  def test_expose_a_cell_outside_of_grid_throws_exception(self):
    self.assertRaises(Exception, self.minesweeper.expose_cell, 50, 50)

  def test_seal_a_cell_outside_of_grid_throws_exception(self):
    self.assertRaises(Exception, self.minesweeper.toggle_seal, 25, 20)

  def test_seal_an_unexposed_cell(self):
    self.minesweeper.toggle_seal(1, 1)

    self.assertEqual(CellState.SEALED, self.minesweeper.get_cell_status(1, 1))

  def test_unseal_a_sealed_cell(self):
    self.minesweeper.toggle_seal(1, 1)

    self.minesweeper.toggle_seal(1, 1)

    self.assertEqual(CellState.UNEXPOSED, self.minesweeper.get_cell_status(1, 1))

  def test_seal_an_exposed_cell(self):
    self.minesweeper.expose_cell(1, 1)

    self.minesweeper.toggle_seal(1, 1)

    self.assertEqual(CellState.EXPOSED, self.minesweeper.get_cell_status(1, 1))

  def test_expose_a_sealed_cell(self):
    self.minesweeper.toggle_seal(1, 1)

    self.minesweeper.expose_cell(1, 1)

    self.assertEqual(CellState.SEALED, self.minesweeper.get_cell_status(1, 1))

  @mock.patch.object(Minesweeper, "expose_neighbors")
  def test_expose_a_cell_calls_expose_neighbors(self, mock):
    self.minesweeper.expose_cell(1, 1)

    mock.assert_called()

  @mock.patch.object(Minesweeper, "expose_neighbors")
  def test_expose_neighbors_not_called_on_already_exposed_cell_when_calling_expose_cell(self, mock):
    self.minesweeper.cell_states[1][1] = CellState.EXPOSED

    self.minesweeper.expose_cell(1, 1)

    mock.assert_not_called()

  @mock.patch.object(Minesweeper, "expose_neighbors")
  def test_expose_neighbors_not_called_on_sealed_cell_when_calling_expose_cell(self, mock):
    self.minesweeper.cell_states[1][1] = CellState.SEALED

    self.minesweeper.expose_cell(1, 1)

    mock.assert_not_called()

  @mock.patch.object(Minesweeper, "expose_cell")
  def test_expose_neighbors_calls_expose_cell_on_neighbors(self, mock):
    calls = [call(3, 3), call(3, 4), call(3, 5), call(4, 3), call(4, 4),
             call(4, 5), call(5, 3), call(5, 4), call(5, 5)]

    self.minesweeper.expose_neighbors(4, 4)

    self.assertEquals(mock.call_args_list, calls)

  @mock.patch.object(Minesweeper, "expose_cell")
  def test_expose_neighbors_on_top_left_cell_calls_expose_only_on_existing_cells(self, mock):
    calls = [call(0, 0), call(0, 1), call(1, 0), call(1, 1)]

    self.minesweeper.expose_neighbors(0, 0)

    self.assertEquals(mock.call_args_list, calls)

  @mock.patch.object(Minesweeper, "expose_cell")
  def test_expose_neighbors_on_bottom_right_cell_calls_expose_only_on_existing_cells(self, mock):
    calls = [call(8, 8), call(8, 9), call(9, 8), call(9, 9)]

    self.minesweeper.expose_neighbors(9, 9)

    self.assertEquals(mock.call_args_list, calls)

  @mock.patch.object(Minesweeper, "expose_cell")
  def test_expose_neighbors_on_border_cell_only_exposes_existing_cells(self, mock):
    calls = [call(0, 4), call(0, 5), call(0, 6),
             call(1, 4), call(1, 5), call(1, 6)]

    self.minesweeper.expose_neighbors(0, 5)

    self.assertEquals(mock.call_args_list, calls)

  def test_if_cell_contains_mine(self):
    self.assertFalse(self.minesweeper.is_mine_at(3, 2))

  def test_if_mined_cell_contains_mine(self):
    self.minesweeper.mined_cells[3][2] = True

    self.assertTrue(self.minesweeper.is_mine_at(3, 2))

  def test_is_mine_at_top_out_of_range(self):
    self.assertFalse(self.minesweeper.is_mine_at(-1, 4))

  def test_is_mine_at_bottom_out_of_range(self):
    self.assertFalse(self.minesweeper.is_mine_at(10, 5))

  def test_is_mine_at_left_out_of_range(self):
    self.assertFalse(self.minesweeper.is_mine_at(5, -1))

  def test_is_mine_at_right_out_of_range(self):
    self.assertFalse(self.minesweeper.is_mine_at(7, 10))

  @mock.patch.object(Minesweeper, "expose_neighbors")
  def test_exposing_adjacent_cell_does_not_call_expose_neighbors(self, mock):
    self.minesweeper.mined_cells[3][4] = True

    self.minesweeper.expose_cell(3, 5)

    mock.assert_not_called()

  def test_cell_with_no_neighboring_mines_has_mines_count_of_0(self):
    self.assertEquals(0, self.minesweeper.adjacent_mines_count_at(4, 6))

  def test_cell_with_one_neighboring_mine_has_mines_count_of_0(self):
    self.minesweeper.mined_cells[3][4] = True

    self.assertEquals(0, self.minesweeper.adjacent_mines_count_at(3, 4))

  def test_cell_with_one_neighboring_mine_has_mines_count_of_1(self):
    self.minesweeper.mined_cells[3][4] = True

    self.assertEquals(1, self.minesweeper.adjacent_mines_count_at(3, 5))

  def test_cell_with_two_neighboring_mines_has_mines_count_of_2(self):
    self.minesweeper.mined_cells[3][4] = True
    self.minesweeper.mined_cells[2][6] = True

    self.assertEquals(2, self.minesweeper.adjacent_mines_count_at(3, 5))

  def test_top_left_corner_cell_with_one_neighboring_mine_has_mines_count_of_1(self):
    self.minesweeper.mined_cells[0][1] = True

    self.assertEquals(1, self.minesweeper.adjacent_mines_count_at(0, 0))

  def test_top_right_corner_cell_with_no_neighboring_mines_has_mine_count_of_0(self):
    self.assertEquals(0, self.minesweeper.adjacent_mines_count_at(0, 9))

  def test_bottom_right_corner_cell_with_one_neighboring_mines_has_mines_count_of_1(self):
    self.minesweeper.mined_cells[9][8] = True

    self.assertEquals(1, self.minesweeper.adjacent_mines_count_at(9, 9))

  def test_bottom_left_corner_cell_with_no_neighboring_mines_has_mines_count_of_0(self):
    self.assertEquals(0, self.minesweeper.adjacent_mines_count_at(9, 0))

  def test_get_game_status(self):
    self.assertEquals(GameStatus.INPROGRESS, self.minesweeper.get_game_status())

  def test_expose_mined_cell_and_game_status_returns_LOST(self):
    self.minesweeper.mined_cells[4][4] = True

    self.minesweeper.expose_cell(4, 4)

    self.assertEquals(GameStatus.LOST, self.minesweeper.get_game_status())

  def test_game_in_progress_after_all_mines_sealed_but_cells_remain_unexposed(self):
    for i in range(self.minesweeper.NUM_MINES):
      self.minesweeper.mined_cells[i][i] = True
      self.minesweeper.cell_states[i][i] = CellState.SEALED

    self.assertEqual(GameStatus.INPROGRESS, self.minesweeper.get_game_status())

  def test_game_in_progress_after_all_mines_are_sealed_but_empty_cell_is_sealed(self):
    for i in range(self.minesweeper.NUM_MINES):
      self.minesweeper.mined_cells[i][i] = True
      self.minesweeper.cell_states[i][i] = CellState.SEALED

    self.minesweeper.cell_states[9][0] = CellState.SEALED

    self.assertEqual(GameStatus.INPROGRESS, self.minesweeper.get_game_status())

  def test_game_in_progress_after_all_mines_are_sealed_but_adjacent_cell_unexposed(self):
    for i in range(self.minesweeper.NUM_MINES):
      self.minesweeper.mined_cells[i][i] = True
      self.minesweeper.cell_states[i][i] = CellState.SEALED
    
    self.minesweeper.cell_states[0][1] = CellState.SEALED

    self.assertEqual(GameStatus.INPROGRESS, self.minesweeper.get_game_status())
  
  def test_all_mines_sealed_and_other_cells_expose_returns_game_status_WON(self):
    for i in range(self.minesweeper.NUM_MINES):
      self.minesweeper.mined_cells[0][i] = True
      self.minesweeper.toggle_seal(0, i)  

    self.minesweeper.expose_neighbors(1, 0)

    self.assertEquals(GameStatus.WON, self.minesweeper.get_game_status())
  
  def test_set_mines_0_initializes_10_mines(self):
    self.minesweeper.set_mines(0)
    self.assertEquals(10, sum(1 for cells in self.minesweeper.mined_cells for is_mine in cells if is_mine))

  def test_set_mines_0_has_at_least_one_different_mine_location_than_set_mines_1(self):
    self.minesweeper.set_mines(0)
    mines_set_with_seed_0 = [mined_cells[:] for mined_cells in self.minesweeper.mined_cells]
    self.minesweeper.mined_cells = [[False for i in range(self.minesweeper.SIZE)] for i in range(self.minesweeper.SIZE)]

    self.minesweeper.set_mines(1)
    mines_set_with_seed_1 = [mined_cells[:] for mined_cells in self.minesweeper.mined_cells]

    self.assertFalse(mines_set_with_seed_0 == mines_set_with_seed_1)


if __name__ == '__main__':
  main()
