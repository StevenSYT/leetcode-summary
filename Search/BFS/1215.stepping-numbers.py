from collections import deque
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        q = deque(list(range(1, 10)))
        res = []
        if low == 0: res.append(0)
        while q:
            cur = q.popleft()
            if low <= cur <= high:
                res.append(cur)
            if cur < high:
                last_digit = cur % 10
                if last_digit > 0:
                    q.append(cur * 10 + last_digit - 1)
                if last_digit < 9:
                    q.append(cur * 10 + last_digit + 1)
        return res  