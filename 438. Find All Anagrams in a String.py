
'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".'''

import collections


class Solution(object):
    def findAnagrams(self, s, p):

        pc = collections.Counter(p)
        slice_str = s[: len(p)]
        sc = collections.Counter(slice_str)

        slice_index = []

        for x in range(0, len(s) - len(p) + 1):
            if x > 0:
                sc[s[x - 1]] -= 1
                sc[s[x + len(p) - 1]] += 1

                if sc[s[x - 1]] == 0:
                    del sc[s[x - 1]]

            if len(sc) == len(pc):
                if sc == pc:
                    slice_index.append(x)

        return slice_index
