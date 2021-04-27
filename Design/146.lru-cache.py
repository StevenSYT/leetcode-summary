#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


# @lc code=start
class Node:
    def __init__(self, val=None, key=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.map = {}
        self.capacity = capacity
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:

        if key in self.map:
            self._move_to_end(self.map[key])
            return self.map[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._move_to_end(node)

        else:
            new_node = Node(value, key)
            self.map[key] = new_node
            self._add_to_end(new_node)
            if len(self.map) > self.capacity:
                del self.map[self.head.next.key]
                self._remove(self.head.next)

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_to_end(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def _move_to_end(self, node):
        self._remove(node)
        self._add_to_end(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
