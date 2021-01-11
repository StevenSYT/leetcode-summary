
from collections import deque
class Solution:
        # 解法1:
        # 看看这个解答说明为什么上界是 max(x, max(forbidden)) + (a + b)
        # https://leetcode-cn.com/problems/minimum-jumps-to-reach-home/solution/dao-jia-de-zui-shao-tiao-yue-ci-shu-zui-duan-lu-zh/
        # 这道题难点就是在于怎么确定上界，然后用一个hash set把visited 和 forbidden的node结合起来，后续bfs的时候
        # 用来限制下一步的搜索。
        def minimumJumps1(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # each element in the queue is a tuple of (step, position, direction)
        q = deque([(0, 0, "")])
        forbids = set(forbidden)
        limit = max(forbidden + [x]) + a + b
        
        while q:
            cur_step, cur_pos, direction = q.popleft()
            if cur_pos == x:
                return cur_step
            forward = cur_pos + a
            backward = cur_pos - b
            if forward not in forbids and cur_pos < limit:
                q.append((cur_step + 1, forward, "+"))
                forbids.add(forward)
            if backward > 0 and backward not in forbids and direction != "-":
                # 这里有个很tricky的点就是，这里不能forbidden，因为后退回cur-b处时，
                # 无法覆盖前进到cur-b再后退到cur-2b的情况。
                # 间接说明了forbidden只存一个pos信息不足，应该包含pos以及到达这个位置时的
                # direction。
                q.append((cur_step + 1, backward, "-"))
                
        return -1
    # 解法2：
    # 区别在于，这个解法上边界只用照顾到max(forbidden + [x]) + b
    # 并且visited里同时记录了(pos, direction)两个状态
    # 然后这里bfs的while loop的一次iteration会把当前q里的点全过一遍，所以step就不用传进queue里了
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # each element in the queue is a tuple of (position, direction)
        q = deque([(0, "+")])
        limit = max(forbidden + [x]) + b
        step = 0
        # each element in visited is a tuple of (position, direction), note that
        # same position with different direction should be considered different states
        # since they could lead to different branches.
        visited = set()
        for forb in forbidden:
            visited.add((forb, "+"))
            visited.add((forb, "-"))
        visited.add((0, "+"))
        while q:
            for _ in range(len(q)):
                pos, direction = q.popleft()
                if pos == x:
                    return step
                forward = pos + a
                backward = pos - b
                if pos <= limit and (forward, "+") not in visited:
                    visited.add((forward, "+"))
                    q.append((forward, "+"))
                if direction != "-" and backward > 0 and (backward, "-") not in visited:
                    q.append((backward, "-"))
                    visited.add((backward, "-"))
            step += 1
        return -1
                
                
        