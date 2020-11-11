# Dynamic Programming

- [状态压缩 DP](#状态压缩-DP)
  - [Stickers To Spell Word](#stickers-to-spell-word)
  - [Smallest Sufficient Team](#smallest-sufficient-team)

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
