'''You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 is s that is equal to the concatenation of any permutation of words.
We return an empty array.
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indices = []
        if s is None or len(s) == 0 or words is None or len(words) == 0:
            return indices
        wordCount = dict()
        for i in range(len(words)):
            if words[i] in wordCount:
                wordCount[words[i]] += 1
            else:
                wordCount[words[i]] = 1
        wordLength = len(words[0])
        wordArrayLength = wordLength * len(words)
        for i in range(0, len(s) - wordArrayLength + 1):
            current = s[i:i + wordArrayLength]
            wordMap = dict()
            index = 0
            j = 0
            while index < len(words):
                part = current[j: j + wordLength]
                if part in wordMap:
                    wordMap[part] += 1
                else:
                    wordMap[part] = 1
                j += wordLength
                index += 1
            if wordMap == wordCount:
                indices.append(i)
        return indices
