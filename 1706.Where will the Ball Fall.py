'''You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.'''
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n_r, n_c = len(grid), len(grid[0])
        answer = list(range(n_c))
        for r in range(n_r):
            for i in range(n_c):
                c= answer[i]
                if c== -1:
                    continue
                c_nxt = c+grid[r][c]
                if c_nxt <0 or c_nxt>= n_c or grid[r][c_nxt] == -grid[r][c]:
                    answer[i] = -1
                    continue
                answer[i] += grid[r][c]
        return answer
            
        
