from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#
# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
#
# algorithms
# Medium (51.29%)
# Total Accepted:    16.7K
# Total Submissions: 32.5K
# Testcase Example:  '"00110"'
#
# A string of '0's and '1's is monotone increasing if it consists of some
# number of '0's (possibly 0), followed by some number of '1's (also possibly
# 0.)
#
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or
# a '1' to a '0'.
#
# Return the minimum number of flips to make S monotone increasing.
#
#
#
#
# Example 1:
#
#
# Input: "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
#
#
#
# Example 2:
#
#
# Input: "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
#
#
#
# Example 3:
#
#
# Input: "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
#
#
#
#
# Note:
#
#
# 1 <= S.length <= 20000
# S only consists of '0' and '1' characters.
#
#
#
#
#


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros = ones = 0
        for c in s:
            if c == '0':
                zeros += 1
            else:
                ones += 1
            """ Our first choice is always flipping 0s to 1s, but in case when there are less 
            1s in the prefix of s, say s = 100011, we should probally flip those 1s. 
            Hence, zeros = min(zeros, ones)
            We keep doing so cause we know, when zeros < ones, the leading 0 are all flipped to 1 .
            And when zeros > ones, the leading 1 are flipper to 0, which always making a monotone string.
            """
            zeros = min(zeros, ones)
        return zeros


sol = Solution()
s = "00011000"
s = "11111"
s = "0101100011"
s = "10011111110010111011"
s = "1"
print(sol.minFlipsMonoIncr(s))
