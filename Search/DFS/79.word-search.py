#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board) == 0:
            return False

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(char_pos, i, j, visited):
            if 0 <= i < m and 0 <= j < n and not visited[i][j] \
               and word[char_pos] == board[i][j]:
                if char_pos == len(word) - 1:
                    return True
                visited[i][j] = True
                res = False
                for dir in dirs:
                    res = res or dfs(char_pos + 1, i + dir[0], j + dir[1],
                                     visited)
                visited[i][j] = False
                return res
            return False

        for i in range(m):
            for j in range(n):
                if dfs(0, i, j, visited):
                    return True
        return False


# @lc code=end
