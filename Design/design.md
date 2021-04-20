# Design
- [Insert Delete GetRandom O(1)](#insert-delete-getrandom-o1)

## Insert Delete GetRandom O(1)

[380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

**Solution**

用一个array + hashmap来做。Hashmap存val to index mapping。Array里存value。然后删除的部分比较巧，先通过hashmap找到index，然后再Array里将其和末尾元素的值互换 (操作为O(1))，然后pop掉末尾元素。

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