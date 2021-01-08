# Tree

- [Traversal](#traversal)
  - [Inorder Successor in BST](#inorder-successor-in-bst)
  - [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)

## Traversal

Includes in-order, pre-order, post-order traversals.

### Inorder Successor in BST

[285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)

**_Solution 1_**

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

**_Solution 2_**

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
