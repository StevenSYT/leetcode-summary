from collections import deque


class Solution:
    def pass_times(self, num_customers, arr_time, direction):
        enter_q = deque()
        exit_q = deque()
        for i in range(len(arr_time)):
            if direction[i] == 0:
                enter_q.append((arr_time[i], i))
            else:
                exit_q.append((arr_time[i], i))
        # print("enter_q:", enter_q)
        # print("exit_q:", exit_q)
        t = 0
        priority = 1
        res = [None for _ in range(num_customers)]
        while enter_q or exit_q:
            exit_waiting = exit_q and exit_q[0][0] <= t
            enter_waiting = enter_q and enter_q[0][0] <= t
            if not exit_waiting and not enter_waiting:
                priority = 1
                t += 1
                continue
            if priority == 1:
                if exit_waiting:
                    res[exit_q.popleft()[1]] = t
                elif enter_waiting:
                    res[enter_q.popleft()[1]] = t
                    priority = 0
            else:
                if enter_waiting:
                    res[enter_q.popleft()[1]] = t
                elif exit_waiting:
                    res[exit_q.popleft()[1]] = t
                    priority = 1
            t += 1
        return res


num_customers = [4, 5]
arr_times = [[0, 0, 1, 5], [0, 1, 1, 3, 3]]
directions = [[0, 1, 1, 0], [0, 1, 0, 0, 1]]
outputs = [[2, 0, 1, 5], [0, 2, 1, 4, 3]]

s = Solution()
pass_count = 0
for i in range(len(num_customers)):
    res = s.pass_times(num_customers[i], arr_times[i], directions[i])
    if (res == outputs[i]):
        pass_count += 1
        print("Test case {} passed.".format(i))
    else:
        print("Test case {} failed".format(i))

if pass_count == len(num_customers):
    print("Accepted, {}/{} passed.".format(pass_count, len(num_customers)))
else:
    print("Wrong answer, {}/{} passed.".format(pass_count, len(num_customers)))
