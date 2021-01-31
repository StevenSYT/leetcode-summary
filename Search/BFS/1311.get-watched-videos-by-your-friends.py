#
# @lc app=leetcode id=1311 lang=python3
#
# [1311] Get Watched Videos by Your Friends
#

# @lc code=start
from collections import deque, Counter


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]],
                               friends: List[List[int]], id: int,
                               level: int) -> List[str]:
        steps = 0
        q = deque([id])
        visited = set()

        while q:
            size = len(q)
            if steps == level:
                break

            for _ in range(size):
                person = q.popleft()
                for friend in friends[person]:
                    if friend not in visited and friend != id:
                        q.append(friend)
                        visited.add(friend)
            steps += 1

        res = []
        while q:
            res.extend(watchedVideos[q.popleft()])
        counter = Counter(res)

        return sorted(counter.keys(), key=lambda x: (counter[x], x))


# @lc code=end
