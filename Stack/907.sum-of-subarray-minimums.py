#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#


# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # https://leetcode.com/problems/sum-of-subarray-minimums/discuss/257811/Python-O(n)-slightly-easier-to-grasp-solution-(explained)
        # [3, 1, 2, 4，1]
        # 分析一下所有以第i个元素结尾的subarray:
        # [3]
        # [3, 1], [1]
        # [3, 1, 2], [1, 2], [2]
        # [3, 1, 2, 4], [1, 2, 4], [2, 4], [4]
        # [3, 1, 2, 4, 2], [1, 2, 4, 2], [2, 4, 2], [4, 2], [2]
        # 对应的最小值之和 result[i]:
        # 3
        # 1 + 1
        # 1 + 1 + 2
        # 1 + 1 + 2 + 4
        # 1 + 1 + 2 + 2 + 2
        # 最终的结果是 sum(result)
        # 这里可以看到对于arr[i-1] <= arr[i] 的情况，result[i] = result[i-1] + arr[i]
        # 如果arr[i-1] > arr[i], 那就要往前看找到第一个满足条件arr[j] <= arr[i]的元素j,
        # 这时候result[i] = result[j] + (i - j) * arr[i], [0, j]的subarray的最小元素不会改变,
        # 然后剩下的[j+1, i]里面生成的subarray的最小元素都是arr[i].
        # 这里要找到比arr[i]小的左边第一个元素, 就要用到单调栈, 并且要用一个单调递增栈。
        arr = [0] + arr
        stack = [0]
        result = [0] * len(arr)
        for i in range(1, len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            stack.append(i)
            result[i] = result[j] + (i - j) * arr[i]
        return sum(result) % (10**9 + 7)


# @lc code=end
