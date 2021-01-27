#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        visited = set()
        # dq: each element is a pair of (steps, x) where x means the x-th
        # square.
        dq = deque([(0, 0)])

        while dq:
            steps, x = dq.popleft()

            if x == n**2 - 1:
                return steps

            if x in visited:
                continue

            visited.add(x)

            for i in range(1, 7):
                if x + i < n**2:
                    nx = x + i

                    # Be careful about the r, c computing
                    r = n - nx // n - 1
                    c = nx % n if (nx // n % 2 == 0) else n - nx % n - 1

                    if board[r][c] != -1:
                        # nx starts from 0, so we need to offset -1 for it.
                        nx = board[r][c] - 1

                    dq.append((steps + 1, nx))

        return -1


# @lc code=end
