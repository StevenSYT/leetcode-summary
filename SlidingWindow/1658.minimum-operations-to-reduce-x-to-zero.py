class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 这道题巧的地方是，转化一下思路，求最少的操作可以
        # 等效为找所有subarray里求和结果等于sum(nums) - x
        # 并且最长的。
        target = sum(nums) - x
        n = len(nums)
        if target < 0:
            return -1
        preSum = 0
        l = 0
        length = -1
        for r in range(n):
            preSum += nums[r]
            # 这里preSum过大就右移左指针
            while l < n and preSum > target:
                preSum -= nums[l]
                l += 1
            if preSum == target:
                length = max(length, r - l + 1)
        # 有可能没找到一个合适的subarray能求和等于sum(nums) - x
        return n - length if length >= 0 else -1