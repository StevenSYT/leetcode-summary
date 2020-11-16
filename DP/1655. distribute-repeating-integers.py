class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        # 有m个customer
        m = len(quantity)
        M = 1 << m
        # 这里做了一个padding，实际num_counts从index = 1开始。
        # 用num_counts的思路是，nums总共有不超过50个不同的value，
        # 所以这里统计每个num的个数就好了，而且这里num本身不重要，
        # num的重复次数才重要。sort一下，把num重复次数按从小到大排列。
        # 并且这里只取了重复个数，直接忽略了num，原因就是解题过程跟
        # num本身没关系。
        num_counts = [0] + sorted(collections.Counter(nums).values())
        n = len(num_counts)

        # dp就是dp[i][state]表示前i个unique num，能够满足state的情况吗。
        # 这里state表示m个customer有哪些要求的quantity得到了满足。
        # 注意dp[i][0]应该总是为True，属于base case.
        dp = [[True] + [False] * (M - 1) for _ in range(n)]
        dp[0][0] = True

        # state_to_quant表示的是一个state对应所有customer其总quantity。
        # 需要这个的原因是，在某一次对于状态s1，我们如果有一个num的count是
        # c，我们需要看看这个num能一次性满足几个customer并将其更新到当前的s1，
        # 那么s1 + s -> s2的这个转移，我们需要一个s，这个s应该是s1的补集的子集。
        # 判断一个s是否满足条件就是看s对应的总quantity是否小于num count c。
        state_to_quant = [0] * M
        for state in range(M):
            # get the total quantity for a certain state
            for i in range(m):
                if state & (1 << i):
                    state_to_quant[state] += quantity[i]

        # 背包问题，拿或者不拿num，然后算这次操作对下一个state的贡献。
        for i in range(1, n):
            for state in range(M):
                if not dp[i - 1][state]: continue
                # 上面介绍了，这里取补集
                to_add = state ^ (M - 1)
                sub = to_add
                # 对补集求子集
                while sub:
                    # 如果这个子集满足要求，那么就将i加给对应的customer，
                    # 并用这个子集更新当前状态.
                    if num_counts[i] >= state_to_quant[sub]:
                        dp[i][state | sub] = True
                    sub = (sub - 1) & to_add
        return dp[n - 1][M - 1]