from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 8 possible directions
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        queue = deque([(0, 0, 1)])  # (row, col, length)
        visited = set([(0, 0)])  # keep track of visited cells
        
        while queue:
            row, col, length = queue.popleft()
            
            if row == n-1 and col == n-1:
                return length
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, length+1))
                    visited.add((new_row, new_col))
        
        return -1
