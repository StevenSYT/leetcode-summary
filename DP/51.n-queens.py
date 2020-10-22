#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = [-1] * n
        self.size = n
        res = []
        self.dfs(queens, 0, [], res)
        return res
    def dfs(self, queens, row, path, res):
        if (row == self.size):
            res.append(path)
            return
        for i in range(self.size):
            queens[row] = i
            if (self.is_safe(queens, row)):
                tmp = '.' * self.size
                self.dfs(queens, row+1, path + [tmp[:i]+'Q'+tmp[i+1:]], res)

    def is_safe(self, queens, row):
        # Check if current row has any conflict with previous rows
        for i in range(row):
            # queen[i] is on the same column as queens[row]
            if (queens[i] == queens[row]): return False 
            # queen[i] and queen[row] are on the same diagonal
            if (abs(queens[i] - queens[row]) == abs(i - row)): return False
        return True
# @lc code=end

