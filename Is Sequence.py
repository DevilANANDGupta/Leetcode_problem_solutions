'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 ''''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j,n=0,len(t)
        for i in s:
            while j<n and t[j]!=i:
                j+=1
            if j>=n:
                return False
            j+=1
        return True
 
