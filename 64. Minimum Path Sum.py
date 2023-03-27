class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # def minPathSum(grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        # fill the first row
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        # fill the first column
        for j in range(1, m):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        # fill the rest of the table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
