'''Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.'''

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        freq   = Counter(t)
        miss   = len(set(t))
        l,  r  = 0, 0
        wl, wr = -1, len(s)
        
        while True:
            if r < len(s) and miss > 0:
                freq[s[r]] -= 1
                if freq[s[r]] == 0: miss -= 1
                r += 1                
            elif l < len(s) and miss <= 0:
                if r-l < wr-wl: wr, wl = r, l
                if freq[s[l]] == 0: miss += 1
                freq[s[l]] += 1
                l += 1
            else:
                break
        
        return s[wl:wr] if wl >= 0 else ""
