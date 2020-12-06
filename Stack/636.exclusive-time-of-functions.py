#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # Corner case: if there is only one function, just check the last
        # log.
        if n == 1:
            return [int(logs[-1].split(":")[-1]) + 1]        

        stack = []
        res = [0] * n
        prev_time = 0
        for log in logs:
            fn, event, t = log.split(":")
            fn, t = int(fn), int(t)

            if event == 'start':
                if stack:
                    res[stack[-1]] += t - prev_time
                    prev_time = t
                stack.append(fn)
            else:
                res[stack.pop()] += t - prev_time + 1
                prev_time = t + 1
        return res

# @lc code=end

