# DFS

[Backtracking](#backtracking) 
- [Subsets](#subsets)
- [Subsets II](#subsets-ii)
- [Permutations](#permutations)

## Backtracking

### Subsets

[78. Subsets](https://leetcode.com/problems/subsets/)

**Solution**

Iterative:

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res
```

Recursive:

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.dfs(0, nums)

    def dfs(self, pos, nums):
        if pos == len(nums):
            return [[]]

        next_pos = self.dfs(pos + 1, nums)

        return next_pos + [[nums[pos]] + subset for subset in next_pos]
```

Backtrack:

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs([], 0, nums, res)
        return res

    def dfs(self, subset, pos, nums, res):
        res.append(subset.copy())

        for i in range(pos, len(nums)):
            subset.append(nums[i])
            self.dfs(subset, i + 1, nums, res)
            # backtrack
            subset.pop()
```

### Subsets II

[90. Subsets II](https://leetcode.com/problems/subsets-ii/)

**Solution**

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        self.dfs([], 0, sorted_nums, res)
        return res
    
    def dfs(self, subset, pos, nums, res):
        res.append(subset.copy())

        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i - 1]:
                continue
            
            subset.append(nums[i])
            self.dfs(subset, i + 1, nums, res)
            # backtrack
            subset.pop()
```


### Permutations

[46. Permutations](https://leetcode.com/problems/permutations/)

**Solution**

很常规的backtrack，注意有两个data structure需要backtrack

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        num_sets = set(nums)
        res = []
        self.dfs([], num_sets, res)
        return res
    
    def dfs(self, path, nums, res):
        if not nums:
            res.append(path.copy())
            return
        
        for num in list(nums):
            path.append(num)
            nums.remove(num)
            self.dfs(path, nums, res)
            # Backtrack
            nums.add(num)
            path.pop()
```