# Hashmap

- [Number of Ways Where Square of Number Is Equal to Product of Two Numbers](#number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers)

## Number of Ways Where Square of Number Is Equal to Product of Two Numbers

[1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/)

```python
from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.getCounts(nums1, nums2) + self.getCounts(nums2, nums1)

    def getCounts(self, nums1, nums2):
        count = 0
        for i in range(len(nums1)):
            target = nums1[i]**2
            operand_map = defaultdict(int)

            for k in range(len(nums2)):
                if nums2[k] in operand_map:
                    count += operand_map[nums2[k]]

                if target % nums2[k] == 0:
                    operand_map[target // nums2[k]] += 1

        return count
```
