# Amazon Fresh is running a promotion in which customers receive prizes for purchasing a secret combination of fruits. The combination will change each day, and the team running the promotion wants to use a code list to make it easy to change the combination. The code list contains groups of fruits. Both the order of the groups within the code list and the order of the fruits within the groups matter. However, between the groups of fruits, any number, and type of fruit is allowable. The term "anything" is used to allow for any type of fruit to appear in that location within the group.
# Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
# Based on the above secret code list, a customer who made either of the following purchases would win the prize:
# orange, apple, apple, banana, orange, banana
# apple, apple, orange, orange, banana, apple, banana, banana
# Write an algorithm to output 1 if the customer is a winner else output 0.

# Input
# The input to the function/method consists of two arguments:
# codeList, a list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.
# shoppingCart, a list of strings representing the order in which a customer purchases fruit.
# Output
# Return an integer 1 if the customer is a winner else return 0.
# Note
# 'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group. 'anything' has to be something, it cannot be "nothing."
# 'anything' must represent one and only one fruit.
# If secret code list is empty then it is assumed that the customer is a winner.


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


code_lists = [[["apple", "apple"], ["banana", "anything", "banana"]],
              [["apple", "apple"], ["banana", "anything", "banana"]],
              [["apple", "apple"], ["banana", "anything", "banana"]],
              [["apple", "apple"], ["apple", "apple", "banana"]]]
shopping_carts = [["orange", "apple", "apple", "banana", "orange", "banana"],
                  ["banana", "orange", "banana", "apple", "apple"],
                  ["apple", "banana", "apple", "banana", "orange", "banana"],
                  ["apple", "apple", "apple", "banana"]]
outputs = [1, 0, 0, 0]

s = Solution()

num_passed = 0
for i in range(len(code_lists)):
    res = s.win_prize(code_lists[i], shopping_carts[i])
    if res == outputs[i]:
        num_passed += 1
        print("Test {} passed.".format(i))
    else:
        print("Test {} failed. Expected: {}, result: {}".format(
            i, outputs[i], res))
        break

if (num_passed != len(code_lists)):
    print("Wrong Answer, ({}/{}) test(s) passed".format(
        num_passed, len(code_lists)))

else:
    print("Accepted")
