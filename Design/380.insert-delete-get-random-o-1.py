#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#


# @lc code=start
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


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
