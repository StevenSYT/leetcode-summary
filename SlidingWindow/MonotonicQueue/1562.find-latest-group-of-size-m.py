#
# @lc app=leetcode id=1562 lang=python3
#
# [1562] Find Latest Group of Size M
#

# @lc code=start
from collections import deque


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return n
        pos_to_step = [None] * (n + 1)
        for s, pos in enumerate(arr):
            pos_to_step[pos] = s + 1

        # Use pos_to_step[] to map the corresponding step that the
        # target pos is flipped.
        #
        # For a possible group [i, i + m -1], assume step t is the last
        # step that all bits in this group is turned '1', this group could be a
        # valid "group" if and only if at step t, bit i-1 and bit i + m are still
        # '0's. =>   'xxx0[111]0xxx'
        #
        # If at step t, that group is a valid group, the last step that it remains
        # valid is min(pos_to_step[i-1], pos_to_step[i + m]) - 1 which is: RIGHT before
        # any one of these '0's turned '1'.
        #
        # The step t is basically the largest value in pos_to_step[i:i+m]. Then we can
        # use a sliding window of size m starting from [0, m-1] and towards right, for each
        # sliding window we need to find the largest value of pos_to_step for each bit, and
        # compare it with the neiboring bits flipping steps. Then this is turned into problem
        # Sliding Window Maximum (https://leetcode.com/problems/sliding-window-maximum/).
        res = -1
        q = deque()
        for r in range(1, n + 1):
            while q and r - q[0] >= m:
                q.popleft()
            # Note that given this problem, there is no way that
            # two different positions will correspond to the same
            # step. So here we can use "<" with no equal sign.
            while q and pos_to_step[q[-1]] < pos_to_step[r]:
                q.pop()
            q.append(r)
            # step t is the last step that all this interval/group of bits
            # are turned into '1's, we then need to compare it with the
            # two neiboring bit outside of the interval and see if we can have
            # a valid step that target group/interval is a valid one.
            if r >= m:
                t = pos_to_step[q[0]]
                left = pos_to_step[r - m] if r - m >= 1 else float('inf')
                right = pos_to_step[r + 1] if r + 1 <= n else float('inf')

                if (left > t and right > t):
                    res = max(res, min(left, right) - 1)
        return res


# @lc code=end
