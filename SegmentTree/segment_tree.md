# Segment Tree & Fenwick Tree

- [Range Sum Query - Mutable](#range-sum-query---mutable)
- [Range Sum Query 2D - Mutable](#range-sum-query-2d---mutable)

## Range Sum Query - Mutable

[307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)

```python
class SegTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.info = 0
        self.left = self.right = None


def buildTree(node, a, b, nums):
    if (a == b):
        node.info = nums[a]
        return

    mid = (a + b) // 2
    node.left = SegTreeNode(a, mid)
    node.right = SegTreeNode(mid + 1, b)
    buildTree(node.left, a, mid, nums)
    buildTree(node.right, mid + 1, b, nums)
    node.info = node.left.info + node.right.info


def updateSingle(node, idx, val):
    if idx < node.start or idx > node.end:
        return

    if node.start == node.end:
        node.info = val
        return

    updateSingle(node.left, idx, val)
    updateSingle(node.right, idx, val)
    node.info = node.left.info + node.right.info


def queryRange(node, a, b):
    if b < node.start or a > node.end:
        return 0

    if a <= node.start and node.end <= b:
        return node.info

    return queryRange(node.left, a, b) + queryRange(node.right, a, b)


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.root = SegTreeNode(0, n - 1)
        buildTree(self.root, 0, n - 1, nums)

    def update(self, index: int, val: int) -> None:
        updateSingle(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return queryRange(self.root, left, right)
```

## Range Sum Query 2D - Mutable

[308. Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/)

**Solution**

花花的视频，讲fenwick tree讲的非常清楚。https://www.youtube.com/watch?v=WbafSgetDDk 

```python
class FenwickTree:
    def __init__(self, m, n):
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]

    def low_bit(self, x):
        return x & (-x)

    def update(self, row, col, delta):
        x = row
        while x < len(self.sums):
            y = col
            while y < len(self.sums[0]):
                self.sums[x][y] += delta
                y += self.low_bit(y)
            x += self.low_bit(x)

    def query(self, row, col):
        x = row
        res = 0
        while x > 0:
            y = col
            while y > 0:
                res += self.sums[x][y]
                y -= self.low_bit(y)
            x -= self.low_bit(x)
        return res

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.fw_tree = FenwickTree(m, n)
        for x in range(m):
            for y in range(n):
                self.fw_tree.update(x + 1, y + 1, matrix[x][y])

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.fw_tree.update(row + 1, col + 1, delta)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        sum += self.fw_tree.query(row2 + 1, col2 + 1) + self.fw_tree.query(row1, col1)
        sum -= self.fw_tree.query(row2 + 1, col1) - self.fw_tree.query(row1, col2 + 1)
        return sum
```
