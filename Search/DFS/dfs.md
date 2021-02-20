# DFS

[Backtracking](#backtracking)

- [Subsets](#subsets)
- [Subsets II](#subsets-ii)
- [Permutations](#permutations)
- [Permutations II](#permutations-ii)
- [Combination Sum](#combination-sum)
- [Combination Sum II](#combination-sum-ii)
- [Combination Sum III](#combination-sum-iii)
- [Letter Case Permutation](#letter-case-permutation)
- [Sudoku Solver](#sudoku-solver)
- [Beautiful Arrangement](#beautiful-arrangement)
- [Word Break II](#word-break-ii)
- [Generate Parenthese](#generate-parenthese)
- [Generalized Abbreviation](#generalized-abbreviation)

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

很常规的 backtrack，注意有两个 data structure 需要 backtrack

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

### Permutations II

[Permutations II](https://leetcode.com/problems/permutations-ii/)

**Solution**

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        self.dfs([], sorted_nums, res)
        return res

    def dfs(self, path, nums, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            self.dfs(path + [nums[i]], nums[:i] + nums[i + 1:], res)
```

### Combination Sum

[39. Combination Sum](https://leetcode.com/problems/combination-sum/)

**Solution**

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(candidates)
        res = []
        self.dfs([], sorted_nums, target, res)
        return res


    def dfs(self, path, nums, target, res):
        if target == 0:
            res.append(path)
            return

        if target < 0:
            return

        for i in range(len(nums)):
            if nums[i] > target:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            self.dfs(path + [nums[i]], nums[i:], target - nums[i], res)
```

### Combination Sum II

[40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

**Solution**

需要注意的一个 trick 就是，在 for loop 里判断一下当前选的 number 是不是比 target 大，如果是提前结束，这样可以达到剪枝的目的。

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(candidates)
        res = []
        self.dfs([], sorted_nums, target, res)
        return res

    def dfs(self, path, nums, target, res):
        if target < 0:
            return

        if target == 0:
            res.append(path)
            return

        for i in range(len(nums)):
            if nums[i] > target:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            self.dfs(path + [nums[i]], nums[i + 1:], target - nums[i], res)
```

### Combination Sum III

[216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

**Solution**

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = range(1, 10)
        res = []
        self.dfs([], nums, k, n, res)
        return res

    def dfs(self, path, nums, k, target, res):
        if k == 0:
            if target == 0:
                res.append(path)
            return

        for i in range(len(nums)):
            if nums[i] > target:
                break

            self.dfs(path + [nums[i]], nums[i + 1:], k - 1, target - nums[i],
                     res)
```

### Letter Case Permutation

[784. Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)

**Solution**

```python
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.dfs('', 0, S, res)
        return res

    def dfs(self, path, pos, string, res):
        if pos == len(string):
            res.append(path)
            return

        if string[pos].isnumeric():
            self.dfs(path + string[pos], pos + 1, string, res)

        else:
            self.dfs(path + string[pos].upper(), pos + 1, string, res)
            self.dfs(path + string[pos].lower(), pos + 1, string, res)
```

### Sudoku Solver

[37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

**Solution**

```python
from collections import defaultdict


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_sets, col_sets, cell_sets = defaultdict(set), defaultdict(
            set), defaultdict(set)

        def get_cell_num(row, col):
            return (row // 3) * 3 + col // 3

        to_fill = []

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    row_sets[r].add(board[r][c])
                    col_sets[c].add(board[r][c])
                    cell_sets[get_cell_num(r, c)].add(board[r][c])
                else:
                    to_fill.append((r, c))

        def dfs(idx, board):
            if idx == len(to_fill):
                return True

            row, col = to_fill[idx]
            cell_num = get_cell_num(row, col)
            for ch in "123456789":
                if ch in row_sets[row] or ch in col_sets[
                        col] or ch in cell_sets[cell_num]:
                    continue

                board[row][col] = ch
                row_sets[row].add(ch)
                col_sets[col].add(ch)
                cell_sets[cell_num].add(ch)

                if dfs(idx + 1, board):
                    return True

                board[row][col] = '.'
                row_sets[row].remove(ch)
                col_sets[col].remove(ch)
                cell_sets[cell_num].remove(ch)

        dfs(0, board)
        return board
```

### Beautiful Arrangement

[526. Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/)

**Solution**

```python

class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))

        return self.dfs([], nums)

    def is_divisible(self, a, b):
        return a // b >= 1 and a % b == 0

    def dfs(self, path, nums):
        if not nums:
            return 1

        res = 0
        i = len(path) + 1

        for idx in range(len(nums)):
            if self.is_divisible(nums[idx], i) or self.is_divisible(
                    i, nums[idx]):
                res += self.dfs(path + [nums[idx]],
                                nums[:idx] + nums[idx + 1:])

        return res
```

### Word Break II

[140. Word Break II](https://leetcode.com/problems/word-break-ii/)

**Solution**

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = self.dfs(s, 0, wordDict, {})
        return res

    def dfs(self, s, pos, wordDict, cache):
        if pos == len(s):
            return [""]
        if pos in cache:
            return cache[pos]
        res = []
        for word in wordDict:
            if self.beginWith(s, pos, word):
                subpaths = self.dfs(s, pos + len(word), wordDict, cache)
                for path in subpaths:
                    delimeter = " " if path else ""
                    res.append(word + delimeter + path)
        cache[pos] = res
        return res

    def beginWith(self, s, pos, target):
        return s[pos:pos + len(target)] == target
```

### Generate Parenthese

[22. Generate Parenthese](https://leetcode.com/problems/generate-parentheses/)

**Solution**

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        self.dfs("", n, [], res)
        return res

    def dfs(self, path, k, stack, res):
        if k == 0 and not stack:
            res.append(path)
            return

        if stack:
            self.dfs(path + stack[-1], k, stack[:-1], res)

        if k > 0:
            self.dfs(path + "(", k - 1, stack + [")"], res)
```

### Generalized Abbreviation

[320. Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation/)

**Solution**

```python
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        self.dfs("", 0, word, 0, res)
        return res

    def dfs(self, path, pos, word, count, res):
        if pos == len(word):
            if count > 0:
                path += str(count)
            res.append(path)
            return

        self.dfs(path, pos + 1, word, count + 1, res)

        self.dfs(path + (str(count) if count > 0 else "") + word[pos], pos + 1,
                 word, 0, res)
```
