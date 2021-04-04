# Binary Search

- [Split Array Largest Sum](#split-array-largest-sum)

## Split Array Largest Sum

[410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/submissions/)
这题用 memo + cumsum + dfs也能过，但是python勉强过。
最优解是二分搜索，而且思想很巧妙，搜索范围是`[max(nums), sum(nums)]`
```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)

        res = 0
        while low <= high:
            mid = (low + high) // 2

            if self.is_valid(nums, m, mid):
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res

    def is_valid(self, nums, m, target):
        num_array = 1
        cur_sum = 0

        for num in nums:
            if cur_sum + num <= target:
                cur_sum += num

            else:
                cur_sum = num
                num_array += 1

        return num_array <= m
```