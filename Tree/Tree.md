# Tree
- [Traversal](#traversal)
    - [Inorder Successor in BST](#inorder-successor-in-bst)

## Traversal
Includes in-order, pre-order, post-order traversals.
### Inorder Successor in BST
[285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)

***Solution 1***

Recursion:

```python
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val < p.val:
            return self.inorderSuccessor(root.right)
        else:
            left = self.inorderSuccessor(root.left)
            return left if left else root
```
