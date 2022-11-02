'''
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

Example 1:

Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
Example 3:

Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3'''

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        def checkNeighbor(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        
        q = deque([start])
        visited = {start}
        ### use extra variable to store mutations
        mutations = 0
        while q:
            ### use for loop to check all nodes in the q
            ### so that after the for loop, we can increment mutations by 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == end:
                    return mutations
                for nei in bank:
                    if checkNeighbor(cur,nei) and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            ### increment mutations by 1
            mutations += 1
        return -1
