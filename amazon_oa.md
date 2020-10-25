# Amazon Online Assessment Questions (2020 October)
  - [Amazon Fresh Promotion](#amazon-fresh-promotion)
  - [Five Star Sellers](#five-star-sellers)
  - [Transaction Logs](#transaction-logs)
  - [Utilization Checks](#utilization-checks)

### Amazon Fresh Promotion 
Amazon Fresh is running a promotion in which customers receive prizes for purchasing a secret combination of fruits. The combination will change each day, and the team running the promotion wants to use a code list to make it easy to change the combination. The code list contains groups of fruits. 

Both the order of the groups within the code list and the order of the fruits within the groups matter. However, between the groups of fruits, any number, and type of fruit is allowable. The term "anything" is used to allow for any type of fruit to appear in that location within the group.
Consider the following secret code list: `[[apple, apple], [banana, anything, banana]]`

Based on the above secret code list, a customer who made either of the following purchases would win the prize:

`orange, apple, apple, banana, orange, banana`

`apple, apple, orange, orange, banana, apple, banana, banana`

Write an algorithm to output 1 if the customer is a winner else output 0.

**Input**

The input to the function/method consists of two arguments:

`codeList`, a list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.

`shoppingCart`, a list of strings representing the order in which a customer purchases fruit.

**Output**

Return an integer 1 if the customer is a winner else return 0.

__Note__

'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group. 'anything' has to be something, it cannot be "nothing."

'anything' must represent one and only one fruit.
If secret code list is empty then it is assumed that the customer is a winner.

```python
class Solution:
    def win_prize(self, code_list, shopping_cart):
        for code in code_list:
            print("shopping_cart: {}".format(shopping_cart))  
            next_shopping_cart = self.match_in_cart(code, shopping_cart)
            
            if (len(next_shopping_cart) == len(shopping_cart)): return 0
            shopping_cart = next_shopping_cart
        return 1

    def match_in_cart(self, code, shopping_cart):
        for i in range(len(shopping_cart) - len(code) + 1):
            found_match = True
            for j in range(len(code)):
                if code[j] != 'anything' and code[j] != shopping_cart[i + j]:
                    found_match = False
                    break
            if found_match:
                print("found match: {}".format(code))
                return shopping_cart[i + len(code):]
        print("did not find a match for {}".format(code))
        return shopping_cart
```

### Five Star Sellers
Given the number of five-star and total reviews for each product a company sells, as well as the threshold percentage, what is the minimum number of additional five-star reviews the company needs to become five star seller.
For ex, there are 3 products (n=3) with `productRatings =[[4,4],[1,2],[3,6]]`, percentage rating `threshold = 77`.

`[1,2]` indicates => [1 (five star reviews) ,2 (total reviews)].

We need to get the seller reach the threshold with minimum number of additional five star reviews.

Before we add more five star reviews, the percentage for this seller is `((4/4) + (1/2) + (3/6))/3 = 66.66%`

If we add a five star review to 2nd product, `((4/4) + (2/3) + (3/6))/3 = 72.22%`

If we add another five star review to 2nd product, `((4/4) + (3/4) + (3/6))/3 = 75%`

If we add a five star review to 3rd product, `((4/4) + (3/4) + (4/7))/3 = 77.38%`

At this point, 77% (threshold) is met. Therefore, answer is 3 (because that is the minimum five star reviews we need to add, to get the seller reach the threshold).

Constraints:
```
1<= productRatings.size() <=200
In product ratings, [fivestar, total], fivestar <=100, total<=100
1<=ratingsThreshold< 100
productRatings contains only non negative integers.
```

Solution: Use a priority queue to store the product ratings, basically we always want to boost the product ratings
by always update the one that increase the average rating most. 

For the metric we can use the difference:  `r[0]+1/r[1]+1 - r[0]/r[1]`, always apply the five start rating to the 
produce that would have the highest increase. 

```python
import heapq
from typing import List


class Solution:
    def min_five_state_reviews(self, product_ratings: List[List[int]],
                               ratings_threshold: int) -> int:
        pq = [(-self.diff(rating), rating)
              for rating in product_ratings]  # O(n)
        heapq.heapify(pq)  # O(n)
        ave_rating = sum(map((lambda x: x[0] / x[1]), product_ratings)) / len(
            product_ratings)  #O(n)
        count = 0  # O(c)
        while ave_rating < ratings_threshold / 100:
            count += 1
            diff, rating = heapq.heappop(pq)  # O(log(n))
            rating = [rating[0] + 1, rating[1] + 1]
            heapq.heappush(pq, (-self.diff(rating), rating))
            ave_rating = sum(map((lambda x: x[1][0] / x[1][1]), pq)) / len(pq)
        return count

    def diff(self, product_rating):
        return (product_rating[0] + 1) / (product_rating[1] + 1) - (
            product_rating[0] / product_rating[1])
```

### Transaction Logs

Amazon parses logs of user transactions/activity to flag fraudulent activity. The log file is represented as an Array of arrays. The arrays consist of the following data:

`[<userid1> <userid2> <# of transactions>]`

For example:

`[345366 89921 45]`

Note the data is space delimited

So, the log data would look like:
`
[
  [345366 89921 45],
[029323 38239 23]
...
]
`

Write a function to parse the log data to find distinct users that meet or cross a certain threshold. The function will take in 2 inputs:

**Input 1**: Log data in form an array of arrays
**Input 2**: threshold as an integer

Output should be an array of userids that are sorted.

If same userid appears in the transaction as userid1 and userid2, it should count as one occurence, not two.

```python
class Solution:
    def transaction_logs(self, logs, threshold):
        user_map = {}
        for log in logs:
            log_arr = log[0].split(" ")
            user_map[log_arr[0]] = user_map.get(log_arr[0], 0) + 1
            if (log_arr[0] != log_arr[1]):
                user_map[log_arr[1]] = user_map.get(log_arr[1], 0) + 1
        target_users = []
        for key, val in user_map.items():
            if (val >= threshold):
                target_users.append(int(key))
        return sorted(target_users, reverse=True)
```

### Utilization Checks
A new Amazon-developed scaling computing system checks the average utilization of the computing system every second while it monitors. It implements an autoscale policy to add or reduce instances depending on the current load as described below. Once an action of adding or reducing the number of instances is performed, the system will stop monitoring for 10 seconds. During that time, the number of instances does not change.

Average utilization < 25%: An action is instantiated to reduce the number of instances by half if the number of instances is greater than 1 (take the ceiling if the number is not an integer). If the number of instances is 1, take no action.

25% <= Average utilization <= 60%: Take no action.

Average utilization > 60%: An action is instantiated to double the number of instances if the doubled value does not exceed 2* 10^8. If the number of instances exceeds this limit upon doubling, perform no action.

Given an array of integers that represent the average utilization at each second, determine the number of instances at the end of the time frame.

**Example**

```
instances = 2
averageUtil = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]
```

At second 1, the average utilization averageUtil[0] = 25 <= 25. Take no action.

At second 2, the average utilization averageUtil[1] = 23 < 25. Reduce the number of instances by half, 2/2 = 1.

Since an action was taken, the system will stop checking for 10 seconds, from averageUtil[2] to averageUtil[11].

At averageUtil[12] = 76, 76 > 60 so the number of instances is doubled from 1 to 2.

There are no more readings to consider and 2 is the final answer.

***Function Description***

Complete the function finallnstances in the editor below.

finallnstances has the following parameter(s):


  `int` instances: an integer that represents the original number of instances running

  `int` averageUtil[n]: an array of integers that represents the average utilization at each second of the time frame

Returns:
   int: an integer that represents the final number of instances running.

**Contraints**
```
1 <= instances <= 10^5
1 <= n < 10^5
0 <= averageUtil[i] <= 100
```

***Solution***
```python
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
```