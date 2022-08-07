'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
               if s == None or t == None:
                    return False
               elif s == "" and t == "":
                  return True
               else:
                   if len(s) != len(t):
                      return False
    
                   lookup = {}   
                   for i in range(0, len(s)):
                       c1 = s[i]
                       c2 = t[i]

                       if c1 in lookup:
                            if lookup[c1] != c2:
                                  return False
                       else:
                           if c2 in lookup.values():
                               return False
                           lookup[c1] = c2

                   return True
            
        
