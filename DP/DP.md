# Dynamic Programming

- [状态压缩 DP](#状态压缩-DP)
  - [Stickers To Spell Word](#stickers-to-spell-word)

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
