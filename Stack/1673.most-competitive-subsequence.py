class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        stack = []
        n = len(nums)
        for i in range(n):
            while stack and len(stack) + (n - i) > k and stack[-1] > nums[i]:
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])
        return stack