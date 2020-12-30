# pylint: disable=unused-variable
import os
import sys
from io import BytesIO, IOBase
import math
import itertools as ITER
from collections import defaultdict as D
from collections import Counter as CO
from collections import deque as Q
import threading
from functools import lru_cache, reduce
from functools import cmp_to_key as CMP
from bisect import bisect_left as BL
from bisect import bisect_right as BR
import random as RA
import cmath, time

# ? Variables

MOD = (10 ** 9) + 7
MA = float("inf")
MI = float("-inf")


# * gui will be here


# * backend code for sudoku
start_time = time.time()


class Sudoku:
    def check_row(self, i, board):
        values = set()
        for k in range(0, 9):
            p = board[i][k]
            if p == 0:
                continue
            if p in values:
                return False
            values.add(p)
        return True

    def check_col(self, j, board):
        values = set()
        for k in range(0, 9):
            p = board[k][j]
            if p == 0:
                continue
            if p in values:
                return False
            values.add(p)
        return True

    def check_sgrid(self, i, j, board):
        x, y = i // 3, j // 3
        has = set()
        for i in range(3):
            for j in range(3):
                ele = board[x + i][y + j]
                if ele in has:
                    return False
                has.add(ele)
        return True

    def IsValidSudoku(self, board):
        def check_sub_grid(i, j):
            values = set()
            for m in range(i, i + 3):
                for n in range(j, j + 3):
                    p = board[n][m]
                    if m == n:
                        if not self.check_row(m, board):
                            return False
                        if not self.check_col(n, board):
                            return False
                    if p == 0:
                        continue
                    if p in values:
                        return False
                    values.add(p)
            return True

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check_sub_grid(i, j):
                    return False
        return True

    # * this is the sudoku generator
    def Sudoku_generator(self, board):
        def next_pos(grid, store):
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == 0:
                        store[0] = i
                        store[1] = j
                        return True
            return False

        def create(grid, row, col):
            for i in range(9):
                for j in range(9):
                    w = grid[i][j]
                    if w != 0:
                        row[i].add(w)
                        col[j].add(w)

        def is_valid(i, j, key, row, col, grid):
            if key in row[i]:
                return False
            if key in col[j]:
                return False
            p = (i // 3) * 3
            q = (j // 3) * 3
            for x in range(3):
                for y in range(3):
                    if grid[x + p][y + q] == key:
                        return False
            return True

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        RA.shuffle(arr)

        def sudoku_solver(row, col, grid):
            store = [0, 0]
            if not next_pos(grid, store):
                return True
            r = store[0]
            c = store[1]
            for i in arr:
                if is_valid(r, c, i, row, col, grid):
                    grid[r][c] = i
                    row[r].add(i)
                    col[c].add(i)
                    if sudoku_solver(row, col, grid):
                        return True
                    grid[r][c] = 0
                    row[r].remove(i)
                    col[c].remove(i)
            return False

        row = D(set)
        col = D(set)
        create(board, row, col)
        sudoku_solver(row, col, board)
        return board


def question(board):

    hint = RA.randint(18, 30)

    totalpos = [(i, j) for i in range(9) for j in range(9)]
    wanted = RA.choices(totalpos, k=hint)
    qs = [[0] * 9 for i in range(9)]

    for i, j in wanted:
        qs[i][j] = board[i][j]

    return qs


def all():
    board = [[0] * 9 for i in range(9)]
    sudokuobj = Sudoku()
    ans = sudokuobj.Sudoku_generator((board))
    return question(ans), ans


