from collections import defaultdict
class Solution:
    def killProcess(self, pid, ppid, kill: int):
        child_map = defaultdict(list)
        for p, pp in zip(pid, ppid):
            child_map[pp].append(p)
        return self.dfs(kill, child_map)

    def dfs(self, target, child_map):
        res = [target]
        for child in child_map[target]:
            res += self.dfs(child, child_map)
        return res

s = Solution()
pid = [1,3,10,5]
ppid = [3,0,5,3]
kill = 5
output = [5,10]

res = s.killProcess(pid, ppid, kill)
if res == output:
    print("Passed.")
else:
    print("Failed.")