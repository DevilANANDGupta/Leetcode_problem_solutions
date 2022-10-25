'''Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true'''

from itertools import zip_longest

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        # [1] here, we construct generators (not lists!) that
        #     yield (!) characters from each word-item
        gen1 = (ch1 for w1 in word1 for ch1 in w1)
        gen2 = (ch2 for w2 in word2 for ch2 in w2)
        
        # [2] zip_longest from itertools ensures that
        #     different lengths are treated correctly
        return all(ch1 == ch2 for ch1, ch2 in zip_longest(gen1, gen2))
