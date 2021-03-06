import tkinter as tk
import os
import sys
from random import random
from itertools import product
sys.path.append(os.path.dirname(__file__).replace("gui", ""))

from minesweeper import Minesweeper, CellState, GameStatus

class MinesweeperGui(tk.Frame):
  SEAL_SYMBOL = "S"
  MINE_SYMBOL = "X"

  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.master.geometry("400x400")
    self.master.title("Minesweeper")
    self.master.rowconfigure(0, weight=1)
    self.master.columnconfigure(0, weight=1)
    self.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    self.initialize_game()
  
  def initialize_game(self):
    self.minesweeper = Minesweeper()
    self.minesweeper.set_mines(random())
    self.create_cell_grid()

  def create_cell_grid(self):
    for i in range(Minesweeper.SIZE):
      self.rowconfigure(i, weight=1)
      self.columnconfigure(i, weight=1)
      for j in range(Minesweeper.SIZE):
        self.create_cell(i, j)

  def create_cell(self, x, y):
    button = tk.Button(self, text="", height=1, width=2, bg="SystemButtonFace", fg="gray1")
    button.bind("<Button-1>", self.left_click)
    button.bind("<Button-2>", self.right_click)
    button.bind("<Button-3>", self.right_click)
    button.grid(row=x, column=y, sticky="nsew")

  def left_click(self, event):
    if self.minesweeper.get_game_status() == GameStatus.INPROGRESS:
      x = event.widget.grid_info()["row"]
      y = event.widget.grid_info()["column"]
      self.minesweeper.expose_cell(x, y)
      self.update_grid()

  def right_click(self, event):
    if self.minesweeper.get_game_status() == GameStatus.INPROGRESS:
      x = event.widget.grid_info()["row"]
      y = event.widget.grid_info()["column"]
      self.minesweeper.toggle_seal(x, y)
      self.update_grid()

  def update_grid(self):
    for i in range(Minesweeper.SIZE):
      for j in range(Minesweeper.SIZE):
        self.update_cell(i, j)
    if self.minesweeper.get_game_status() == GameStatus.WON:
      self.show_win_dialog()
    elif self.minesweeper.get_game_status() == GameStatus.LOST:
      self.show_all_mines()
      self.show_lose_dialog()

  def update_cell(self, x, y):
    cell = self.grid_slaves(row=x, column=y)[0]

    if self.minesweeper.get_cell_status(x, y) == CellState.EXPOSED:
      cell.configure(state="disabled", relief="sunken", bg="light grey")

      adjacent_mines_count = self.minesweeper.adjacent_mines_count_at(x, y)
      if self.minesweeper.is_mine_at(x, y):
        cell.configure(state="disabled", text=self.MINE_SYMBOL)
      elif adjacent_mines_count:
        cell.configure(state="disabled", text=adjacent_mines_count)
      else:
        cell.configure(state="disabled", text="")

    elif self.minesweeper.get_cell_status(x, y) == CellState.SEALED:
      cell.configure(state="disabled", text=self.SEAL_SYMBOL, bg="cyan")
    else:
      cell.configure(state="normal", text="", bg="SystemButtonFace")

  def show_lose_dialog(self):
    frame = tk.Frame(self, width=1, height=2, bg="red3")
    for i in range(2):
      frame.rowconfigure(i, weight=1)
      frame.columnconfigure(i, weight=1)
    dialog = tk.Label(frame, width=3, height=2, bg="red3", fg="gray1", text="You lost!")
    reset_button = tk.Button(frame, text="Restart", command=self.initialize_game)
    quit_button = tk.Button(frame, text="Quit", command=self.master.destroy)
    dialog.grid(row=0, column=0, columnspan=2, sticky="nsew")
    reset_button.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
    quit_button.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
    frame.place(relx=0.5, rely=0.5, anchor="center", relheight=0.25, relwidth=0.25)

  def show_win_dialog(self):
    frame = tk.Frame(self, width=1, height=2, bg="green3")
    for i in range(2):
      frame.rowconfigure(i, weight=1)
      frame.columnconfigure(i, weight=1)
    dialog = tk.Label(frame, width=3, height=2, bg="green3", fg="gray1", text="You won!")
    reset_button = tk.Button(frame, text="Restart", command=self.initialize_game)
    quit_button = tk.Button(frame, text="Quit", command=self.master.destroy)
    dialog.grid(row=0, column=0, columnspan=2, sticky="nsew")
    reset_button.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
    quit_button.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
    frame.place(relx=0.5, rely=0.5, anchor="center", relheight=0.25, relwidth=0.25)
  
  def show_all_mines(self):
    for x, y in product(range(self.minesweeper.SIZE), range(self.minesweeper.SIZE)):
      if self.minesweeper.is_mine_at(x, y):
        self.grid_slaves(row=x, column=y)[0].configure(state="disabled", text=self.MINE_SYMBOL, relief="groove", disabledforeground="red")


if __name__ == "__main__":
  root = tk.Tk()
  app = MinesweeperGui(master=root)
  app.mainloop()
