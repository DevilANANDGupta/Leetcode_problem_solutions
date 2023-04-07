class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
    # def numEnclaves(grid):
    # """
    # :type grid: List[List[int]]
    # :rtype: int
    # """
    # get dimensions of the grid
        m = len(grid)
        n= len(grid[0])
        
        # function to perform dfs from a given cell
        def dfs(i, j):
            # mark current cell as visited
            grid[i][j] = 0
            
            # perform dfs on adjacent land cells
            for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    dfs(ni, nj)
        
        # perform dfs on boundary cells
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if grid[i][j] == 1:
                        dfs(i, j)
        
        # count remaining land cells
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        
        return count
