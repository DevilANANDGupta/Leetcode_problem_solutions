'''Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl,pl = len(s), len(p)
        S_1, P_1 = None,None
        si=pi=0
        while si < sl:
            
            if pi<pl and (p[pi]=="?" or s[si]==p[pi]):
                si+=1
                pi+=1
            elif pi<pl and p[pi]=="*":
                S_1, P_1 = si,pi
                pi+=1
            elif S_1 is not None:
                si,pi = S_1+1, P_1
            else:
                return False
        
        while pi<pl:
            if p[pi]!="*":
                return False
            pi+=1
        return True
        
