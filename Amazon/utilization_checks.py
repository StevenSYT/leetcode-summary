# A new Amazon-developed scaling computing system checks the average utilization of the computing system every second while it monitors. It implements an autoscale policy to add or reduce instances depending on the current load as described below. Once an action of adding or reducing the number of instances is performed, the system will stop monitoring for 10 seconds. During that time, the number of instances does not change.

# Average utilization < 25%: An action is instantiated to reduce the number of instances by half if the number of instances is greater than 1 (take the ceiling if the number is not an integer). If the number of instances is 1, take no action.
# 25% <= Average utilization <= 60%: Take no action.
# Average utilization > 60%: An action is instantiated to double the number of instances if the doubled value does not exceed 2* 10^8. If the number of instances exceeds this limit upon doubling, perform no action.
# Given an array of integers that represent the average utilization at each second, determine the number of instances at the end of the time frame.

# Example

# instances = 2
# averageUtil = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]

# At second 1, the average utilization averageUtil[0] = 25 <= 25. Take no action.
# At second 2, the average utilization averageUtil[1] = 23 < 25. Reduce the number of instances by half, 2/2 = 1.
# Since an action was taken, the system will stop checking for 10 seconds, from averageUtil[2] to averageUtil[11].
# At averageUtil[12] = 76, 76 > 60 so the number of instances is doubled from 1 to 2.
# There are no more readings to consider and 2 is the final answer.
# Function Description

# Complete the function finallnstances in the editor below.

# finallnstances has the following parameter(s):
#    int instances: an integer that represents the original number of instances running
#    int averageUtil[n]: an array of integers that represents the average utilization at each second of the time frame

# Returns:
#    int: an integer that represents the final number of instances running.

# Contraints

# 1 <= instances <= 10^5
# 1 <= n < 10^5
# 0 <= averageUtil[i] <= 100

import math
from typing import List


class Solution:
    def final_instances(self, instances: int, average_util: List[int]) -> int:
        """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """
        i = 0
        sleep = 0
        while i < len(average_util):
            if sleep != 0:
                sleep -= 1
                i += 1
                continue
            if (average_util[i] < 25):
                instances = math.ceil(instances / 2)
                sleep = 10
            elif (average_util[i] > 60 and instances < 10**8):
                instances *= 2
                sleep = 10
            i += 1
        return instances


instances = [2, 2]
average_utils = [[25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80],
                 [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]]
output = [2, 2]

s = Solution()
for i in range(len(instances)):
    assert s.final_instances(instances[i], average_utils[i]) == output[i]
