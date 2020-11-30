#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        self.nodes = {}
        return self.clone(node)
        
    def clone(self, node):
        if node.val in self.nodes:
            return self.nodes[node.val]
        copy = Node(node.val)
        self.nodes[copy.val] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(self.clone(neighbor))
        return copy

# @lc code=end

