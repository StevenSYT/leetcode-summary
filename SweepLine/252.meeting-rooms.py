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