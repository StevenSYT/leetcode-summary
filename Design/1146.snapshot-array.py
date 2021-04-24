#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#


# @lc code=start
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


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end
