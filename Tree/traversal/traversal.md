# Traversal

- [Preoder](#preorder)
  - [Binary Tree Preorder Traversal](#binary-tree-preoder-traversal)
  - [Flip Binary Tree To Match Preorder Traversal](#flip-binary-tree-to-match-preorder-traversal)
  - [Verify Preorder Serialization of a Binary Tree](#verify-preoder-serialization-of-a-binary-tree)
- [Inorder](#inorder)
  - [Inorder Successor in BST](#inorder-successor-in-bst)
  - [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
  - [Recover Binary Search Tree](#recover-binary-search-tree)

- [Construct Binary Tree from Preorder and Inorder Traversal](#construct-binary-tree-from-preorder-and-inorder-traversal)
- [Construct Binary Tree from Inorder and Postorder Traversal](#construct-binary-tree-from-inorder-and-postorder-traversal)

## Preorder

### Binary Tree Preorder Traversal

[144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

**Solution**

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res

```

### Flip Binary Tree To Match Preorder Traversal

[971. Flip Binary Tree To Match Preorder Traversal](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/)

**Solution**

这题就是考察dfs，后续补上stack/iterative的写法

```python
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.i = 0
        self.res = []
        return self.res if self.dfs(root, voyage) else [-1]
        
        
    def dfs(self, root, voyage):
        if not root:
            return True
        
        if root.val != voyage[self.i]:
            return False

        self.i += 1

        if root.left and root.left.val != voyage[self.i]:
            self.res.append(root.val)
            return self.dfs(root.right, voyage) and self.dfs(root.left, voyage)

        else:
            return self.dfs(root.left, voyage) and self.dfs(root.right, voyage)
```

### Verify Preorder Serialization of a Binary Tree

[331. Verify Preorder Serialization of a Binary Tree](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/)

**Solution**

We just need to remember how many empty slots we have during the process.

Initially we have one ( for the root ).

for each node we check if we still have empty slots to put it in.

- a null node occupies one slot.
- a non-null node occupies one slot before he creates two more. the net gain is one.

```python
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1

        for node in preorder.split(","):
            if slots == 0:
                return False

            if node == "#":
                slots -= 1

            else:
                slots += 1

        return slots == 0
```

## Inorder

### Inorder Successor in BST

[285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)

**Solution 1**

Recursive:

```python
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right)
        else:
            left = self.inorderSuccessor(root.left)
            return left if left else root
```

**Solution 2**

Iterative:

```python
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = None
        while root:
            if not root:
                return res
            if root.val <= p.val:
                root = root.right
            else:
                res = root
                root = root.left
        return res

```

### Binary Tree Inorder Traversal

[94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

**_Solution 1_**

Recursive

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return None
        res = []
        left = self.inorderTraversal(root.left)
        if left:
            res += left
        res.append(root.val)
        right = self.inorderTraversal(root.right)
        if right:
            res += right
        return res
```

**_Solution 2_**

Iterative

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(TreeNode(cur.val))
                stack.append(cur.left)
            else:
                res.append(cur.val)
        return res
```

### Recover Binary Search Tree

[99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)

**Solution**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, prev, swaps, stack = root, TreeNode(float("-inf")), [], []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack.pop()
            if node.val < prev.val:
                swaps.append((prev, node))

            prev, cur = node, node.right

        swaps[0][0].val, swaps[-1][1].val = swaps[-1][1].val, swaps[0][0].val
```

### Construct Binary Tree from Preorder and Inorder Traversal
[105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

**Solution**

这题得记一记。思路很清楚，但是很巧。思路就是，假设当前从 inorder 的 index i~j 之间遍历，从 preorder 里找到当前 traverse 的 root node，然后将其 map 到 inorder 的 index k，这样[i, k - 1]就是 root node 的左边的子树，[k + 1, j]就是右边的子树。如此递归下去。

```python
from collections import deque


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_dict = {val: idx for idx, val in enumerate(inorder)}
        preorder = deque(preorder)

        def helper(start, end):
            if start > end:
                return None

            cur_node = TreeNode(preorder.popleft())
            idx = inorder_dict[cur_node.val]
            cur_node.left = helper(start, idx - 1)
            cur_node.right = helper(idx + 1, end)

            return cur_node

        return helper(0, len(inorder) - 1)
```

### Construct Binary Tree from Inorder and Postorder Traversal

[106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

**Solution**

这题跟105基本上代码都一样，唯一的区别是postorder遍历的顺序是pop最后一个，这样出来的顺序是root, right, left。所以helper function里要先遍历右边。 

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_dict = {val: idx for idx, val in enumerate(inorder)}

        def helper(start, end):
            if start > end:
                return None

            cur_node = TreeNode(postorder.pop())
            idx = inorder_dict[cur_node.val]
            cur_node.right = helper(idx + 1, end)
            cur_node.left = helper(start, idx - 1)

            return cur_node

        return helper(0, len(inorder) - 1)
```

