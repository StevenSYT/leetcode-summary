# Design

- [Insert Delete GetRandom O(1)](#insert-delete-getrandom-o1)
- [Insert Delete GetRandom O(1) - Duplicates allowed](#insert-delete-getrandom-o1---duplicates-allowed)

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
