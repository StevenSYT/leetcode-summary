#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#


# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def atMost(k):
            counter = collections.Counter()
            l = 0
            res = 0
            for r in range(len(A)):
                counter[A[r]] += 1
                while len(counter) > k:
                    counter[A[l]] -= 1
                    if counter[A[l]] == 0:
                        del counter[A[l]]
                    l += 1
                res += r - l + 1
            return res

        return atMost(K) - atMost(K - 1)


# @lc code=end
