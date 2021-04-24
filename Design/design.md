# Design

- [Insert Delete GetRandom O(1)](#insert-delete-getrandom-o1)
- [Insert Delete GetRandom O(1) - Duplicates allowed](#insert-delete-getrandom-o1---duplicates-allowed)
- [All O`one Data Structure](#all-oone-data-structure)
## Insert Delete GetRandom O(1)

[380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

**Solution**

用一个 array + hashmap 来做。Hashmap 存 val to index mapping。Array 里存 value。然后删除的部分比较巧，先通过 hashmap 找到 index，然后再 Array 里将其和末尾元素的值互换 (操作为 O(1))，然后 pop 掉末尾元素。

```python
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = defaultdict(int)
        self.vals = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.lookup:
            return False

        idx = len(self.vals)
        self.vals.append(val)
        self.lookup[val] = idx
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.lookup:
            return False

        idx = self.lookup[val]
        last_idx = len(self.vals) - 1
        last_val = self.vals[-1]
        self.vals[idx], self.vals[last_idx] = self.vals[last_idx], self.vals[
            idx]
        self.lookup[last_val] = idx
        del self.lookup[val]
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randrange(len(self.vals))
        return self.vals[idx]
```

## Insert Delete GetRandom O(1) - Duplicates allowed

[381. Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)

**Solution**

和 380 非常像，但是 look up map 要用一个 int to set。别的操作没啥变化。注意 remove 里面，如果 set remove 以后为空要记得要删除 entry。

```python
from collections import defaultdict
from random import randrange


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.val_to_idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        res = val not in self.val_to_idx
        idx = len(self.vals)
        self.val_to_idx[val].add(idx)
        self.vals.append(val)
        return res

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.val_to_idx:
            return False

        idx, last_val = self.val_to_idx[val].pop(), self.vals[-1]
        if len(self.val_to_idx[val]) == 0:
            del self.val_to_idx[val]

        self.vals[idx] = last_val
        self.val_to_idx[last_val].add(idx)
        self.val_to_idx[last_val].remove(len(self.vals) - 1)
        if len(self.val_to_idx[last_val]) == 0:
            del self.val_to_idx[last_val]

        self.vals.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        idx = randrange(len(self.vals))
        return self.vals[idx]
```

## All O`one Data Structure

[432. All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/)

**Solution**

这题比较难，需要用到DoubleLinkedList和两个hashmap，一个hashmap负责统计key count，一个hashmap负责count和Node的对应关系。

双链表的一个Node存所有count为x的key，然后maintain一个顺序就是链表最末端存最大，最始端存最小。快速查找到一个node就用那个负责count和Node对应关系的hashmap。

```python
from collections import defaultdict

# Node定义双链表的一个节点，每个节点存一个key的集合
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
```