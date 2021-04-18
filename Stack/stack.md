# Stack
- [Expression Parsing](#expression-parsing)
    - [Build Binary Expression Tree From Infix Expression](#build-binary-expression-tree-from-infix-expression)


## Expression Parsing

### Build Binary Expression Tree From Infix Expression

[1597. Build Binary Expression Tree From Infix Expression](https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/)

**Solution** 

这题跟Basic Calculator III几乎一样，典型的expression parsing的题

```python
class Solution:
    def expTree(self, s: str) -> 'Node':
        ops, vals = [], []
        for ch in s:
            if ch == "(":
                ops.append(ch)
            
            elif ch in "+-*/":
                while ops and self.compare(ops[-1], ch):
                    cur_node = Node(ops.pop())
                    cur_node.right = vals.pop()
                    cur_node.left = vals.pop()
                    vals.append(cur_node)
                
                ops.append(ch)
            
            elif ch == ")":
                while ops[-1] != "(":
                    cur_node = Node(ops.pop())
                    cur_node.right = vals.pop()
                    cur_node.left = vals.pop()
                    vals.append(cur_node)
                
                ops.pop() # pop out the "(" operator
            
            else:
                vals.append(Node(ch))
        
        while ops:
            cur_node = Node(ops.pop())
            cur_node.right = vals.pop()
            cur_node.left = vals.pop()
            vals.append(cur_node)
        
        return vals[-1]
    
    def compare(self, op1, op2):
        if op1 == "(":
            return False
    
        return op1 in "*/" or op2 in "+-"
```