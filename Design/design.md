# Design

- [Insert Delete GetRandom O(1)](#insert-delete-getrandom-o1)
- [Insert Delete GetRandom O(1) - Duplicates allowed](#insert-delete-getrandom-o1---duplicates-allowed)
- [All O`one Data Structure](#all-oone-data-structure)
- [Snapshot Array](#snapshot-array)
- [Design a Stack With Increment Operation](#design-a-stack-with-increment-operation)
- [LRU Cache](#lru-cache)
- [LFU Cache](#lfu-cache)

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

这题比较难，需要用到 DoubleLinkedList 和两个 hashmap，一个 hashmap 负责统计 key count，一个 hashmap 负责 count 和 Node 的对应关系。

双链表的一个 Node 存所有 count 为 x 的 key，然后 maintain 一个顺序就是链表最末端存最大，最始端存最小。快速查找到一个 node 就用那个负责 count 和 Node 对应关系的 hashmap。

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

## Snapshot Array

[1146. Snapshot Array](https://leetcode.com/problems/snapshot-array/)

**Solution**

用一个 map[index, snap_id] = val 来存，get 的时候对 snap_id 做递减的操作，每个循环检查[index, snap_id]是不是在 map 里。map 只有在 set 的时候会被 update，所以有时候 snap 了，某些 index 上对应的值一直没变化的话只会存一个老的 snap_id + index 的 combo

```python
class SnapshotArray:
    def __init__(self, length: int):
        self.map = {}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.map[self.snap_id, index] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        for id in range(snap_id, -1, -1):
            if (id, index) in self.map:
                return self.map[id, index]
        return 0
```

## Design a Stack With Increment Operation

[1381. Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/)

```python
class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.capacity = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.capacity:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i == len(self.stack):
                break

            self.stack[i] += val

```

## LRU Cache

[146. LRU Cache](https://leetcode.com/problems/lru-cache/)

**Solution**

经典题，双链表 + map

```python
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
```

## LFU Cache

[460. LFU Cache](https://leetcode.com/problems/lfu-cache/)

**Solution**

用两个 map + DoubleLinkedList，一个 map 存 key_to_node，一个 map 存 freq_to_list。每个 DoubleLinkedList 存某个 frequency 下所有的 node。详细参考[这个解答](https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list)

```python
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
```
