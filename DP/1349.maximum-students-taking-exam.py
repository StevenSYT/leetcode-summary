#
# @lc app=leetcode id=1349 lang=python3
#
# [1349] Maximum Students Taking Exam
#


# @lc code=start
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        M = len(seats)
        N = len(seats[0])

        dp = [0] * (1 << N)

        def count(cur_state):
            res = 0
            while cur_state:
                res += (cur_state & 1)
                cur_state = (cur_state >> 1)
            return res

        # if 11010 indicates broken seats for "1"s,
        # if any state 01000 & 11010 != 0, that means this
        # state conflicts with the seats.
        seatMasks = [0] * (M + 1)
        for i in range(1, M + 1):
            mask = 0
            for j in range(N):
                if seats[i - 1][j] == '#':
                    mask += (1 << (N - j - 1))
                seatMasks[i] = mask
        for row in range(1, M + 1):
            dp_prev = dp
            dp = [0] * (1 << N)
            for cur_state in range(1 << N):
                # e.g. 1110 & 0111 = 0110 which is not valid state.
                if (cur_state & (cur_state >> 1) != 0 or
                    (seatMasks[row] & cur_state)) != 0:
                    continue

                # Trying to get the dp[cur_state] value
                for prev_state in range(1 << N):
                    # choose a valid prev_state
                    if (prev_state &
                        (prev_state >> 1)) != 0 or (seatMasks[row - 1]
                                                    & prev_state) != 0:
                        continue

                    # e.g. prev_state: 01010
                    #      cur_state:  00100
                    # prev_state&(cur_state>>1) => 01010 & 00010 != 0
                    # cur_state&(prev_state>>1) => 00100 & 00101 != 0
                    # conflict, continue
                    if (prev_state &
                        (cur_state >> 1)) != 0 or (cur_state &
                                                   (prev_state >> 1)) != 0:
                        continue

                    dp[cur_state] = max(dp_prev[prev_state] + count(cur_state),
                                        dp[cur_state])

        return max(dp)


# @lc code=end
