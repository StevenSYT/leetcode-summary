class Solution:
    def numberOfItems(self, s, startIndices, endIndices):
        res = []
        self.cache = {}
        for i in range(len(startIndices)):
            res.append(self.get_num_items(s[startIndices[i] -
                                            1:endIndices[i]]))
        print("res: ", res)
        return res

    def get_num_items(self, s):
        print(s)
        left = s.find('|')
        right = s.rfind('|')
        if left == -1 or left == right:
            return 0
        if (left, right) in self.cache:
            return self.cache[(left, right)]
        count = 0
        for i in range(left, right + 1):
            count += 1 if s[i] == "*" else 0
        self.cache[(left, right)] = count
        return count


strings = ['|**|*|*']
startIndices = [[1, 1]]
endIndices = [[5, 6]]
outputs = [[2, 3]]

s = Solution()
pass_count = 0
for i in range(len(strings)):
    res = s.numberOfItems(strings[i], startIndices[i], endIndices[i])
    if (res == outputs[i]):
        pass_count += 1
        print("Test case {} passed".format(i))
    else:
        print("Test case {} failed".format(i))

pass_status = "Accepted" if pass_count == len(strings) else "Wrong answer"
print("{}, {}/{} passed".format(pass_status, pass_count, len(strings)))