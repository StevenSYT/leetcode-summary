# Sweep Line Algorithm

- [Meeting Rooms](#meeting-rooms)
- [Meeting Rooms II](#meeting-rooms-ii)

## Meeting Rooms

[252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)

**Solution**

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        points = []
        for interval in intervals:
            points.append((interval[0], 1))
            points.append((interval[1], -1))

        cnt = 0
        for point in sorted(points):
            cnt += point[1]
            if cnt > 1:
                return False

        return True
```

## Meeting Rooms II

[253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

**Solution**

```python
class Solution:
    # Sweeping line algorithm.
    # Time: O(nlogn) Space: O(n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = []

        for interval in intervals:
            points.append((interval[0], 1))
            points.append((interval[1], -1))

        cnt, res = 0, 0
        for point in sorted(points):
            cnt += point[1]
            res = max(cnt, res)

        return res
```
