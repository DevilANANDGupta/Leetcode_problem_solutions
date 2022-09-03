'''Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,'''
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result  = []
        if n== 1: result.append(0)
        def dfs(num , n):
            if n ==0:
                result.append(num)
                return 
            last_digit = num%10 
            if last_digit >= k:
                dfs(num*10 + last_digit -k, n-1)
            if k > 0 and last_digit + k < 10: dfs(num*10 + last_digit + k, n-1)
        for d in range(1,10):
            dfs(d, n-1)
        return result
