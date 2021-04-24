#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#

# @lc code=start
from collections import defaultdict


class Node:
    def __init__(self):
        self.key_set = set()
        self.prev = None
        self.next = None

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)

    def get_any_key(self):
        return next(iter(self.key_set))

    def is_empty(self):
        return len(self.key_set) == 0


class DoubleLinkedList:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def insert_after(self, node):
        new_node = Node()
        next_node = node.next
        node.next = new_node
        new_node.prev = node

        new_node.next = next_node
        next_node.prev = new_node

    def insert_before(self, node):
        new_node = Node()
        prev_node = node.prev
        node.prev = new_node
        new_node.next = node

        prev_node.next = new_node
        new_node.prev = prev_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get_first(self):
        return self.head.next

    def get_last(self):
        return self.tail.prev

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def is_empty(self):
        return self.get_first().is_empty()


class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll = DoubleLinkedList()
        self.key_count = Counter()
        self.count_to_node = defaultdict(Node)
        self.count_to_node[0] = self.dll.get_head()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        count = self.key_count[key]
        node = self.count_to_node[count]
        self.key_count[key] += 1

        if count + 1 in self.count_to_node:
            self.count_to_node[count + 1].add_key(key)

        else:
            self.dll.insert_after(node)
            self.count_to_node[count + 1] = node.next
            node.next.add_key(key)

        if count > 0:
            node.remove_key(key)
            if node.is_empty():
                self.dll.remove(node)
                del self.count_to_node[count]

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.key_count:
            count = self.key_count[key]
            node = self.count_to_node[count]
            node.remove_key(key)
            if count == 1:
                del self.key_count[key]

            else:
                self.key_count[key] -= 1
                if count - 1 in self.count_to_node:
                    self.count_to_node[count - 1].add_key(key)

                else:
                    self.dll.insert_before(node)
                    self.count_to_node[count - 1] = node.prev
                    node.prev.add_key(key)

            if node.is_empty():
                del self.count_to_node[count]
                self.dll.remove(node)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return "" if self.dll.is_empty() else self.dll.get_last().get_any_key()

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return "" if self.dll.is_empty() else self.dll.get_first().get_any_key(
        )


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end
