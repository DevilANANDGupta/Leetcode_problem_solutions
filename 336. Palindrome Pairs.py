'''Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]'''



class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word2index, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, postfix = word[:j], word[j:]
                if prefix in word2index and i != word2index[prefix] and postfix == postfix[::-1]:
                    res.append([i, word2index[prefix]])
                if j > 0 and postfix in word2index and i != word2index[postfix] and prefix == prefix[::-1]:
                    res.append([word2index[postfix], i])
        return res
        
