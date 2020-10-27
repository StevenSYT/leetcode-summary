class Solution:
    def substr_of_size_k(self, input_string, num):
        left, right = 0, num
        if num >= len(input_string):
            return []

        res = []
        while right <= len(input_string):
            if (len(set(input_string[left:right])) == num - 1):
                res.append(input_string[left:right])
            left += 1
            right += 1
        return res


input_strings = ["awaglk", "democracy", "wawaglknagagwunagkwkwagl"]
nums = [4, 5, 4]
outputs = [["awag"], ["ocrac", "cracy"],
           ["awag", "naga", "gagw", "gkwk", "wkwa"]]

s = Solution()
pass_count = 0
for i in range(len(input_strings)):
    result = s.substr_of_size_k(input_strings[i], nums[i])
    if (result == outputs[i]):
        print("Test case {} passed".format(i))
        pass_count += 1
    else:
        print("Test case {} failed".format(i))
if pass_count == len(input_strings):
    print("Accepted, {}/{} passed".format(pass_count, len(input_strings)))
else:
    print("Wrong Answer, {}/{} passed".format(pass_count, len(input_strings)))
