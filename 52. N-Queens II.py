'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1'''


class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        pos=set()
        neg=set()
        res=0
        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
                return 
            for c in range(n):
                if c in col or (r+c) in pos or (r-c) in neg:
                    continue
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                backtrack(r+1)
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
        
        backtrack(0)
        # r +=1
        return res 
