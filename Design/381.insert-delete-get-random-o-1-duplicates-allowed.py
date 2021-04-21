#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

# @lc code=start
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


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
