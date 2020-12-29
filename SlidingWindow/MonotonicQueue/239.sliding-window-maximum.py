#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = deque(), []
        # Use the first element of the deque to store the largest element
        # of the window.
        # The q would store candidates of the maximum numbers just in case the largest
        # element is removed after sliding the window.
        for i, num in enumerate(nums):
            # Remove all the element in the q that's smaller that the newly added element,
            # This way we can guarantee that the front of the queue is always the largest one.
            while q and nums[q[-1]] < num:
                q.pop()
            # It is guaranteed that q[-2] >= q[-1] (if len(q) > 1)
            q.append(i)
            while i - q[0] >= k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
        
# @lc code=end

