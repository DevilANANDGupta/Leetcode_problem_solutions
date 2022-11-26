class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs, n = sorted(zip(startTime, endTime, profit)), len(startTime) # [1] prepare jobs for binary search
        dp = [0] * (n + 1)                                         #     by sorting them by start time
        for i in reversed(range(n)):                               # [2] knapsack: either try next job or
            k = bisect_left(jobs, jobs[i][1], key=lambda j: j[0])  #     take this one together with trying
            dp[i] = max(jobs[i][2] + dp[k], dp[i+1])               #     the next valid one
        return dp[0]
