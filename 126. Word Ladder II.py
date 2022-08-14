
'''
4339
508
Add to List
Share
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.'''
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        abc='abcdefghijklmnopqrstuvwxyz'
        wordList=[beginWord]+wordList
        start=0
        try:
            end=wordList.index(endWord)
        except:
            return []
        n=len(wordList)
        l=len(beginWord)
        conn=[[] for i in range(n)]
        d=dict()
        for i in range(n):
            d[wordList[i]]=i
        for i in range(n):
            for j in range(l):
                for k in range(len(abc)):
                    s=wordList[i][:j]+abc[k]+wordList[i][j+1:]
                    if d.get(s,-1)>=0:
                        conn[i].append(d[s])
        valid=[0]*n
        valid[start]=1
        step=1
        wordbag=[[start],[]]
        path=[[] for i in range(n)]
        path[start]=[[beginWord]]
        while len(wordbag[1-step%2])>0:
            step+=1
            wordbag[1-step%2]=[]
            for i in wordbag[step%2]:
                for j in conn[i]:
                    if valid[j]==0 or valid[j]==step:
                        if valid[j]==0:
                            wordbag[1-step%2].append(j)
                        valid[j]=step
                        for k in path[i]:
                            path[j].append(k+[wordList[j]])
            if valid[end]>0:
                break
        return path[end]
