# Binary Search

- [Split Array Largest Sum](#split-array-largest-sum)
- [Koko Eating Bananas](#koko-eating-bananas)
- [Minimum Number of Days to Make m Bouquets](#minimum-number-of-days-to-make-m-bouquets)
- [Find the Smallest Divisor Given a Threshold](#find-the-smallest-divisor-given-a-threshold)

## Split Array Largest Sum

[410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/submissions/)
这题用 memo + cumsum + dfs 也能过，但是 python 勉强过。
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

## Koko Eating Bananas

[875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        res = 0
        while low <= high:
            mid = (low + high) // 2
            if self.valid(piles, h, mid):
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res

    def valid(self, piles, h, k):
        hrs = 0
        for pile in piles:
            hrs += pile // k
            if pile % k != 0:
                hrs += 1

        return hrs <= h
```

## Minimum Number of Days to Make m Bouquets

[1482. Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)

```python
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low, high = min(bloomDay), max(bloomDay)
        res = -1

        while low <= high:
            mid = (low + high) // 2
            if self.canMake(bloomDay, m, k, mid):
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res

    def canMake(self, bloomDay, m, k, mid):
        cum_sum = 0
        num_b = 0

        for bloom in bloomDay:
            if bloom <= mid:
                # is available
                cum_sum += 1

            else:
                cum_sum = 0

            if cum_sum == k:
                num_b += 1
                cum_sum = 0

        return num_b >= m
```

## Find the Smallest Divisor Given a Threshold

[1283. Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)

```python
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)

        res = 0
        while low <= high:
            mid = (low + high) // 2
            if self.is_valid(nums, threshold, mid):
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res

    def is_valid(self, nums, threshold, div):
        return sum(math.ceil(num / div) for num in nums) <= threshold
```