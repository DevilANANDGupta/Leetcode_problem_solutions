'''Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return[]
        start_row,end_row,start_col,end_col = 0,len(matrix),0,len(matrix[0])
        output=[]
        while start_row<end_row or start_col<end_col:
            if start_row<end_row:
                output.extend([matrix[start_row][i] for i in range(start_col,end_col)])
            start_row +=1
            if start_col<end_col:
                output.extend([matrix[i][end_col-1] for i in range(start_row, end_row)])
            end_col -=1
            if start_row<end_row:
                output.extend([matrix[end_row-1][i] for i in range(end_col-1,start_col-1,-1)])
            end_row -=1
            if start_col<end_col:
                output.extend([matrix[i][start_col] for i in range(end_row-1,start_row-1,-1)])
            start_col +=1
        return output
