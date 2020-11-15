# Dynamic Programming

- [状态压缩 DP](#状态压缩-DP)
  - [Stickers To Spell Word](#stickers-to-spell-word)
  - [Smallest Sufficient Team](#smallest-sufficient-team)
  - [Find the Shortest Superstring](#find-the-shortest-superstring)
  - [Maximum Students Taking Exam](#maximum-students-taking-exam)
  - [Parallel Courses II](#parallel-courses-ii)
  - [Number of Ways to Wear Different Hats to Each Other](#number-of-ways-to-wear-different-hats-to-each-other)

## 状态压缩 DP

### Stickers To Spell Word

[LC 691. Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word/)

**_Solution 1_**
Use n bits to store the status.

For example, if n is 5, and target is "hello". `00110` means that "ll" is spelled. 00110 => 6 as an integer value. We can do a bottom up dp trying to get 00000 => 11111 (final status).

```python
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        N = (1 << n)
        # Use n bits to store the status.
        # For example, if n is 5, and target is "hello",
        # 00110 means that "ll" is spelled.
        # 00110 => 6 as an integer value.
        # We can do a bottom up dp trying to get 00000 => 11111 (final status)
        dp = [float('inf')] * N
        dp[0] = 0

        # Building the dp in a bottom up manner
        for i in range(N):
            if dp[i] == float('inf'):
                continue
            for sticker in stickers:
                j = self.findNextStatus(i, target, sticker)
                if j == i: continue
                dp[j] = min(dp[j], dp[i] + 1)
        return -1 if dp[-1] == float('inf') else dp[-1]

    def findNextStatus(self, status, target, sticker):
        for ch in sticker:
            for i in range(len(target)):

                # Check if the i-th char in target is spelled or not
                # and if current ch matches the i-th char in target
                if ((status >> i) & 1) == 0 and target[i] == ch:

                    # Found one valid char, use it and update the status
                    status += (1 << i)

                    # Break out of the inner loop so that current "ch" will
                    # only be used once from the sticker.
                    break
        return status
```

**_Solution 2_**

We can use BFS to solve this problem. Starting from the target string, for each sticker, get the substring after applying the sticker to target string (remove the chars that are spelled using the sticker). Do the BFS until the remaining substring is empty string, return the number stickers used in order to get that substring.

We can use a (target, count) tuple as an element to be stored in the queue for BFS.

```python
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # queue stores a collection of (target, count) tuples.
        # target: the remaining substring to be spelled.
        # count: the number stickers used so far
        queue = deque([(target, 0)])

        while queue:
            cur_target, count = queue.popleft()
            for sticker in stickers:
                next_target = cur_target
                if next_target[0] not in sticker:
                    continue
                for ch_s in sticker:
                    for idx, ch in enumerate(next_target):
                        # If we find a char matching from the sticker,
                        # update the target and move on to next char of the
                        # sticker.
                        # We need to make sure each char in sticker can be
                        # used at most one time.
                        if ch == ch_s:
                            next_target = next_target[:idx] + next_target[idx +
                                                                          1:]
                            break
                if next_target == "":
                    return count + 1
                queue.append((next_target, count + 1))
        return -1
```

### Smallest Sufficient Team

[LC 1125. Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/)

**_Solution 1_**

Use BFS again and it is surprisingly fast.

```python
from collections import deque


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str],
                               people: List[List[str]]) -> List[int]:
        queue = deque([(set(req_skills), set())])

        while queue:
            target_skills, cur_team = queue.popleft()
            for idx, person in enumerate(people):
                if idx in cur_team:
                    continue
                # We need solve/remove all skills in the skillset,
                # so why not just only care about people who has
                # the first skill in target_skills.
                # note that since we cannot index through set, we need
                # to use this next(iter(S)) to access one item in set.
                # TC for next(iter(S)) is O(1) --- needs confirmation.
                if next(iter(target_skills)) not in person:
                    continue
                next_target = target_skills.copy()
                for skill in person:
                    if skill in next_target:
                        next_target.remove(skill)
                if len(next_target) == 0:
                    return cur_team | {idx}
                queue.append((next_target, cur_team | {idx}))
```

**_Solution 2_**

Use bitmask to solve this.

The idea is to iterate through each person, get the binary representation of
this person's skill, and use an integer to store it. Use bottom-up dp, for each
existing entry, try applying this person's skill set to it and update the value
with the optimal one.

dp here is a dict, with status as the key, optimal team as the value.

For the status, we use binary number indicating the status of the
completion of the skill set.

For example if req_skill has 5 elements, 10010 can indicate one status
of the completion of the skill set: the first and the fourth skills are covered
with the current team.

```python
class Solution1:
    def smallestSufficientTeam(self, req_skills: List[str],
                               people: List[List[str]]) -> List[int]:
        n = len(req_skills)

        # Create a mapping from skill to skill index, this will be useful to use the bitmask
        skill_set = {skill: idx for idx, skill in enumerate(req_skills)}

        # dp here is a dict, with status as the key, optimal team as the value.

        # For the status, we use binary number indicating the status of the
        # completion of the skill set.

        # For example if req_skill has 5 elements, 10010 can indicate one status
        # of the completion of the skill set: the first and the fourth skills are covered
        # with the current team.
        dp = {0: []}

        for idx, person in enumerate(people):
            person_skills = 0
            for skill in person:
                # skip skills not in the skill_set.
                if skill not in skill_set:
                    continue
                i = skill_set[skill]
                # update his_skill using bit operation.
                person_skills += 1 << i
            for status, team in list(dp.items()):
                next_status = status | person_skills
                # No new skill can be covered from this person, skip.
                if next_status == status:
                    continue
                # update the dp with new entry or better entry for target status.
                if next_status not in dp or len(
                        dp[next_status]) > len(dp[status]) + 1:
                    dp[next_status] = team + [idx]
        return dp[(1 << n) - 1]
```

### Find the Shortest Superstring

[943. Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/)

**_Solution_**

这是一道旅行商问题 TSP(Traveling Salesman Problem)。对于两个 string S1, S2, S1 -> S2 的距离指的是从 S1 加多少个 char，这个结果的 string 就包含 S2 了。

假设有 string A='abc', B='bcd', C='cde', 那么 A -> B = 1 因为 A 再加一个 char 'd'就能包含 B 了。

同理有： B -> C = 1, A -> C = 2, B -> A = 3, C -> A = 3, C -> B = 3.

dp[status][last]： 当前状态为 status 并且最后一个访问的 city 是 last，存的值为当前的最优 super string。

状态转移：dp[status][last] = dp[status - last] + dis[sec_last][last] 选一个 sec_last 使行走的 distance 最小

```python
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        N = len(A)
        M = (1 << N)

        def distance(a, b):
            for i in range(min(len(a), len(b)), 0, -1):
                if a[-i:] == b[:i]:
                    return len(b) - i
            return len(b)

        def combine(a, b):
            for i in range(min(len(a), len(b)), 0, -1):
                if a[-i:] == b[:i]:
                    return a + b[i:]
            return a + b

        # 这是一道旅行商问题TSP(Traveling Salesman Problem)。
        # 对于两个string S1, S2, S1 -> S2的距离指的是从S1加多少个char，这个结果的string就包含S2了。
        # 假设有string A='abc', B='bcd', C='cde', 那么 A -> B = 1 因为A再加一个char 'd'就能包含B了，
        # 同理有： B -> C = 1, A -> C = 2, B -> A = 3, C -> A = 3, C -> B = 3.
        # dp[status][last]： 当前状态为status并且最后一个访问的city是last，存的值为当前的最优super string
        dp = [[float('inf')] * N for _ in range(M)]
        parent = [[-1] * N for _ in range(M)]
        dis = [[0] * N for _ in range(N)]

        # Get distances
        for i in range(N):
            for j in range(N):
                if i != j:
                    dis[i][j] = distance(A[i], A[j])
        # Base cases: if start with string i, the super string is i itself.
        for i in range(N):
            dp[1 << i][i] = len(A[i])

        # 状态转移：dp[status][last] = dp[status - last] + dis[sec_last][last] 选一个sec_last使行走的distance最小
        for status in range(M):
            for last in range(N):
                if (status & (1 << last)) == 0: continue
                prev_status = status ^ (1 << last)
                if prev_status == 0: continue
                for sec_last in range(N):
                    if (prev_status & (1 << sec_last)) == 0: continue
                    # Choose from the second last node to go from.
                    if dp[status][last] > dp[prev_status][sec_last] + dis[
                            sec_last][last]:

                        dp[status][last] = dp[prev_status][sec_last] + dis[
                            sec_last][last]
                        parent[status][last] = sec_last
        start = min(enumerate(dp[M - 1]), key=lambda x: x[1])[0]
        path = deque([start])

        status = M - 1
        while parent[status][start] != -1:
            prev = parent[status][start]
            path.appendleft(prev)
            status -= (1 << start)
            start = prev
        res = A[start]
        for i in range(1, len(path)):
            res = combine(res, A[path[i]])
        return res
```

### Maximum Students Taking Exam

[1349. Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/)

**_Solution_**

这道题核心思想是用一个二维 dp 矩阵表示状态：`dp[i][s]`表示前 i 行的座位下，第 i 行座位选 s 的坐法，能坐下的最多的学生数。这里 s 用一个二进制数表示，比如 5 人一行，10100，1 表示这个位置有人坐，0 表示不坐。
这样就容易推出来 dp 的转移方程为：

```
dp[i][s] = max(dp[i-1][k] for k in [valid states at row i-1])
```

关于判断 valid 与否，有几个要考虑的因素：

1. 每个学生左右不能再挨着另一个学生，判断方法：将 state 右移一位，如果移动后与原 state 做与运算不能得到 0，说明有相邻位为 1，则是不 valid 的情况。(11000 & 01100 = 01000 != 0)

2. 每个学生左前或右前不能坐人，判断方法，需要判断前后两个状态 s1 和 s2，需要满足(s1>>1)&s2 和 (s2>>1)&s1 都为 0 才是 valid 的情况。

3. 当前状态必须满足坐的学生都坐在能坐的座位上，如果有学生坐在椅子是坏的座位上也不能满足。要判断这个需要先把 input 里的 seats 做一个 bit 的加工，也转化成二进制表示，可以用 1 表示坏的椅子，0 表示好的椅子，那么如果 state&seatsMask 不为 0 的话，表示有学生坐在坏的椅子上了，比如椅子：01100，坐法：00100，01100 & 10100 = 00100 这个“1”就是坐在坏椅子上的学生。

```python
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        M = len(seats)
        N = len(seats[0])

        dp = [0] * (1 << N)

        def count(cur_state):
            res = 0
            while cur_state:
                res += (cur_state & 1)
                cur_state = (cur_state >> 1)
            return res

        # if 11010 indicates broken seats for "1"s,
        # if any state 01000 & 11010 != 0, that means this
        # state conflicts with the seats.
        seatMasks = [0] * (M + 1)
        for i in range(1, M + 1):
            mask = 0
            for j in range(N):
                if seats[i - 1][j] == '#':
                    mask += (1 << (N - j - 1))
                seatMasks[i] = mask
        for row in range(1, M + 1):
            dp_prev = dp
            dp = [0] * (1 << N)
            for cur_state in range(1 << N):
                # e.g. 1110 & 0111 = 0110 which is not valid state.
                if (cur_state & (cur_state >> 1) != 0 or
                    (seatMasks[row] & cur_state)) != 0:
                    continue

                # Trying to get the dp[cur_state] value
                for prev_state in range(1 << N):
                    # choose a valid prev_state
                    if (prev_state &
                        (prev_state >> 1)) != 0 or (seatMasks[row - 1]
                                                    & prev_state) != 0:
                        continue

                    # e.g. prev_state: 01010
                    #      cur_state:  00100
                    # prev_state&(cur_state>>1) => 01010 & 00010 != 0
                    # cur_state&(prev_state>>1) => 00100 & 00101 != 0
                    # conflict, continue
                    if (prev_state &
                        (cur_state >> 1)) != 0 or (cur_state &
                                                   (prev_state >> 1)) != 0:
                        continue

                    dp[cur_state] = max(dp_prev[prev_state] + count(cur_state),
                                        dp[cur_state])

        return max(dp)
```

### Parallel Courses II

[1494. Parallel Courses II](https://leetcode.com/problems/parallel-courses-ii/)

**_Solution_**

这个[解答](https://www.acwing.com/file_system/file/content/whole/index/content/1063233/)讲的很好。

用一个`state`来表示所有的上课的情况，`'0000'`表示都没上，`'1111'`表示都上了。

`dp[state]`表示达到这个状态 state 最少需要的学期数。

状态转移的思路是从一个当前 valid 的状态，得出学生一学期能上的所有的课的组合 (total number <= k)，然后更新下一个状态。

```python
dp[cur_state | new_courses] = min(dp[cur_state | new_courses], dp[cur_state] + 1)
```

注意有几个很巧的小 trick：

1. 得到一个状态 state 所有的子集:

```python
sub = state
while sub:
    print(sub)
    sub = (sub - 1) & state
```

2. 判断一个课的所有 dependency，做一个辅助的 list 存每个课的 dependency 对应的掩码:

```python
deps = [0] * n
for x, y in dependencies:
    deps[y-1] |= (1 << (y-1))
```

代码：

```python
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]],
                             k: int) -> int:
        # '1111' -> 所有的课上完了
        # '0000' -> 一门都没上
        N = 1 << n
        dp = [float('inf')] * N

        # dp[state]: 当达到state的时候，最少需要多少学期
        dp[0] = 0

        # pres[i]: 第i门课的先修课有哪些
        pres = [0] * n
        for dep in dependencies:
            pres[dep[1] - 1] += (1 << (dep[0] - 1))

        # 有效的状态一定是递增
        for cur_state in range(N):
            if dp[cur_state] == float('inf'): continue
            can_study = 0
            for subject in range(n):
                if not (cur_state >> subject) & 1: continue
                if (cur_state & pres[subject]) == pres[subject]:
                    can_study |= (1 << subject)
            if bin(can_study).count('1') <= k:
                dp[can_study | cur_state] = min(dp[can_study | cur_state],
                                                dp[cur_state] + 1)
            else:
                sub = can_study
                while sub > 0:
                    if (bin(sub).count('1') <= k):
                        dp[sub | cur_state] = min(dp[sub | cur_state],
                                                  dp[cur_state] + 1)
                    sub = ((sub - 1) & can_study)  # 从can_study遍历一遍所有的子集，这个操作可以记住
        return dp[N - 1]
```

### Number of Ways to Wear Different Hats to Each Other

[1434. Number of Ways to Wear Different Hats to Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/)

**_Solution_**

**Assign hats to people, don't assign people with hats.**

这道题给的条件很特殊，1 <= n <= 10, number of hats = 40.

这样的话我们知道如果 mask 表示成用了哪些帽子的话，这个数量级就比用 mask 表示哪些人带了帽子。这里要做一个新的映射：hat_to_people，记录的就是每个帽子有哪些人可以戴。

这道题用二维 dp 好理解一些：dp[i][mask]表示如果只用前 i 个帽子，在 mask 这种状态的时候有多少种戴法。这样就 i 以次递增然后如果前 i-1 个帽子的所有情况都算完了，对于第 i 个帽子，根据 hat_to_people 看看这个帽子有哪些人可以戴上它，以及当前 mask 这个人 p 是不是已经带了帽子了。状态转移为：

```
dp[i][mask | (1 << p)] += dp[i-1][mask]
```

```python
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        N = (1 << n)
        mod = 10**9 + 7

        h_to_p = [[] for _ in range(40)]
        for p in range(n):
            for h in hats[p]:
                h_to_p[h - 1].append(p)

        dp = [0] * N
        dp[0] = 1

        for h in range(40):
            for state in range(N - 1, -1, -1):
                for p in h_to_p[h]:
                    if (state & (1 << p) == 0):
                        dp[state | (1 << p)] = (dp[state |
                                                   (1 << p)] + dp[state]) % mod
        return dp[-1]

```
