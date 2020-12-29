import heapq


class Solution:
    # 用priority queue的解法更好理解一些
    # 思路就是用priority queue里存当前index前的k个元素，
    # 队的顶部存前k个元素的accumulated score的最大值，然后当前位置的最大score
    # 就等于pq顶accumulated score最大值加上当前score。
    # 然后pq要有一个remove的过程，就是如果pq[0]已经不在当前index的前k个元素的时候，
    # 就要直接去掉。
    # 时间复杂度 O(NlogN) 空间复杂度O(N)
    def maxResult1(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        q = [(-dp[0], 0)]
        heapq.heapify(q)

        for i in range(1, N):
            while q and i - q[0][1] > k:
                heapq.heappop(q)
            dp[i] = dp[q[0][1]] + nums[i]
            heapq.heappush(q, (-dp[i], i))
        return dp[N - 1]

    # It is more efficient to use a monotonic queue
    # to maintain the maximum value of the k
    # elements prior to i because the append/remove is
    # O(1) for deque.
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # dp存的是到每一个位置当前的最佳score
        dp = [0] * N
        dp[0] = nums[0]
        q = collections.deque([0])

        for i in range(1, N):
            # 每一个时刻q[0]里存的都是i的前k个元素里，score最大的值
            # 这里就可以得到dp[i]的值
            dp[i] = dp[q[0]] + nums[i]
            while q and i - q[0] >= k:
                q.popleft()

            # 这个while loop稍微tricky一点，就是
            # 保证q存的index对应的dp里的值是单调递减的，这样dp[q[0]]才会是最大值
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            q.append(i)

        return dp[N - 1]