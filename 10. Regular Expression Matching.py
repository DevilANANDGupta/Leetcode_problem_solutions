'''Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".'''




class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        DP = [[False for j in range(n+1)] for i in range(m+1)]  
        DP[0][0] = True
        
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1]=="*":
                    DP[i][j] = DP[i][j-2] or i>0 and DP[i-1][j] and (s[i-1]==p[j-2] or p[j-2]==".")
                else:
                    DP[i][j] = i>0 and DP[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]==".")
        
        return DP[-1][-1]
                
       
