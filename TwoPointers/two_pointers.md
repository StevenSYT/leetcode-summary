# Two Pointers

- [Two Sum II - Input array is sorted](#two-sum-ii---input-array-is-sorted)
- [Sum of Square Numbers](#sum-of-square-numbers)
- [Reverse Vowels of a String](#reverse-vowels-of-a-string)
- [Valid Palindrome II](#valid-palindrome-ii)
- [Merge Sorted Array](#merge-sorted-array)
- [Number of Subsequences That Satisfy the Given Sum Condition](#number-of-subsequences-that-satisfy-the-given-sum-condition)

## Two Sum II - Input array is sorted

[167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

**Solution:**

Use left and right pointers. Since the array is sorted, move the left pointer right if the current sum is less than target, move the right pointer left if the current sum is larger than target.

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum > target:
                right -= 1
            elif cur_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]
```

## Sum of Square Numbers

[633. Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/description/)

**solution:**

Need to compute a range of candidate numbers that we can choose from
to do the square sum. Intuitively the upper bound of the candidate would be
the square root of the target number. Then the rest of the code is converted to `Two Sum II - Input array is sorted`

## Reverse Vowels of a String

[345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

**Solution:** Store all vowels `aeiouAEIOU` in a lookup string. Use two pointer to do the reversion.

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        chars = [ch for ch in s]
        l, r = 0, len(chars) - 1
        while l < r:
            if chars[l] in vowels and chars[r] in vowels:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
                continue
            if chars[l] not in vowels:
                l += 1
            if chars[r] not in vowels:
                r -= 1
        return ''.join(chars)
```

## Valid Palindrome II

[680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)

**Solution:**

Use left and right pointers and check whether for each time `s[left] == s[right]`, if at one iteration `s[left] != s[right]`, we can try deleting either `s[left]` or `s[right]`, just check whether the remaining substrings with s[left] or s[right] removed is palindrome. We can write a helper function `isPalindrome` to check.

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1])
            l += 1
            r -= 1
        return True

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

```

## Merge Sorted Array

[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)

**Solution:**

Place the numbers in-place. Use two pointers for each sorted array. Use a pointer for the final list (initial value `m + n - 1`).

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        p = m + n - 1
        while p >= 0:
            if p1 < 0:
                nums1[p] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                nums1[p] = nums1[p1]
                p1 -= 1
            elif nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
```

## Number of Subsequences That Satisfy the Given Sum Condition

[1498. Number of Subsequences That Satisfy the Given Sum Condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        A = sorted(nums)

        l, r = 0, len(A) - 1
        mod = 10**9 + 7
        res = 0

        while l <= r:
            if A[l] + A[r] > target:
                r -= 1

            else:
                # There are 2 ^ (r - l) subsequences for subarray A[l] ~ A[r]
                # with A[l] always in the subsequences. Basically
                # for A[l + 1] ~ A[r] the items can either be picked or not,
                # hence the computation. And each of these subsequence is
                # guarenteed to be a legit one, because:
                # (A[l] + max of the subsequence) < A[l] + A[r] <= target
                res += 2**(r - l) % mod
                l += 1

        return res % mod
```
