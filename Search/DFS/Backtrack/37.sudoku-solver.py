#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from collections import defaultdict


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_sets, col_sets, cell_sets = defaultdict(set), defaultdict(
            set), defaultdict(set)

        def get_cell_num(row, col):
            return (row // 3) * 3 + col // 3

        to_fill = []

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    row_sets[r].add(board[r][c])
                    col_sets[c].add(board[r][c])
                    cell_sets[get_cell_num(r, c)].add(board[r][c])
                else:
                    to_fill.append((r, c))

        def dfs(idx, board):
            if idx == len(to_fill):
                return True

            row, col = to_fill[idx]
            cell_num = get_cell_num(row, col)
            for ch in "123456789":
                if ch in row_sets[row] or ch in col_sets[
                        col] or ch in cell_sets[cell_num]:
                    continue

                board[row][col] = ch
                row_sets[row].add(ch)
                col_sets[col].add(ch)
                cell_sets[cell_num].add(ch)

                if dfs(idx + 1, board):
                    return True

                board[row][col] = '.'
                row_sets[row].remove(ch)
                col_sets[col].remove(ch)
                cell_sets[cell_num].remove(ch)

        dfs(0, board)
        return board


# @lc code=end
