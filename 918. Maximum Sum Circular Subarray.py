from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """
        Kadane's Algorithm
        Two cases:
        1. normal max subarray within A
        2. circular one, that both A[0] and A[n-1] is included
        (A0 + A1 + .. + Ai) + (Aj + ... + An-1)
        = sum(A) - (Ai+1 + ... + Aj-1)
        """
        ret1 = self.max_subarray(A)
        ret2 = sum(A) + self.max_subarray([-a for a in A[1:-1]])  # max negative (-1)
        return max(ret1, ret2)

    def max_subarray(self, A) -> int:
        """
        dp[i] = A[i] + max(dp[i-1],0)
        """
        mx = -float('inf')
        cur = 0
        for a in A:
            cur = a + max(cur, 0)  # RHS cur is the prev
            mx = max(mx, cur)
        return mx

    def maxSubarraySumCircular_error(self, A: List[int]) -> int:
        """
        keep a cur_sum with index, when negative, go back to 0
        """
        cur = [0, None]
        mx = -float('inf')
        i = 0
        j = 0
        n = len(A)
        while i < n:
            cur[0] += A[i]
            cur[1] = i
            mx = max(mx, cur[0])
            j = i + 1
            while cur[0] >= 0 and j < i + n:
                cur[0] += A[j % n]
                mx = max(mx, cur[0])
                j += 1

            i = j

        return mx
