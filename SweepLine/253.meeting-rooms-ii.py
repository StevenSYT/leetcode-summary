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