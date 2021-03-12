# Sweep Line Algorithm

- [Meeting Rooms](#meeting-rooms)
- [Meeting Rooms II](#meeting-rooms-ii)
- [My Calendar III](#my-calendar-iii)

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

## My Calendar III

[732. My Calendar III](https://leetcode.com/problems/my-calendar-iii/)

```python
class MyCalendarThree:
    def __init__(self):
        self.points = []

    def book(self, start: int, end: int) -> int:
        self.points.append((start, 1))
        self.points.append((end, -1))
        self.points.sort()

        cnt = 0
        res = 0
        for point in self.points:
            cnt += point[1]
            res = max(cnt, res)

        return res
```
