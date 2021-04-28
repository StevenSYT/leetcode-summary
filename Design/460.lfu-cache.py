#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#


# @lc code=start
class Node:
    def __init__(self, key=None, val=None):
        self.val = val
        self.key = key
        self.freq = 1
        self.prev = self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def add_node(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def remove_node(self, node=None):
        if self.size == 0:
            return

        if not node:
            # remove the least recently used
            node = self.tail.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

    def is_empty(self):
        return self.size == 0


class LFUCache:
    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.freq_to_list = collections.defaultdict(DoubleLinkedList)
        self.min_freq = 0
        self.capacity = capacity

    def _update_cache(self, node):
        dlist = self.freq_to_list[node.freq]
        dlist.remove_node(node)
        if dlist.is_empty() and node.freq == self.min_freq:
            self.min_freq += 1

        node.freq += 1
        self.freq_to_list[node.freq].add_node(node)

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._update_cache(node)
            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._update_cache(node)

            node.val = value
        else:
            if len(self.key_to_node) == self.capacity:
                removed_node = self.freq_to_list[self.min_freq].remove_node()
                del self.key_to_node[removed_node.key]

            node = Node(key, value)
            self.min_freq = 1
            self.freq_to_list[1].add_node(node)
            self.key_to_node[key] = node


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
