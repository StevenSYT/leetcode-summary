#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#


# @lc code=start
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


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end
