'''Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1'''

class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n+1)
        for nm in range(2, n+1):
            total = 0
            for r in range(1, nm+1):
                left = r-1
                right = nm-r
                total += numTree[left]* numTree[right]
            numTree[nm] = total
        return numTree[n]
