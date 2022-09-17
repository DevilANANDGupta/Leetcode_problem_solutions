'''Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.'''


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(90)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num= int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    box_id = i // 3*3 + j // 3
                    boxes[box_id].add(num)
        def backtrack(i,j):
            nonlocal solved
            if i == 9:
                solved = True
                return 
            new_i = i + (j+1)//9
            new_j = (j+1) % 9
            if board[i][j] != '.':
                backtrack(new_i, new_j)
            else:
                for num in range(1, 10):
                    box_id = i//3 *3 +j //3
                    if num not in rows[i] and num not in cols[j] and num not in boxes[box_id]:
                        rows[i].add(num)
                        cols[j].add(num)
                        boxes[box_id].add(num)
                        board[i][j] = str(num)
                        backtrack(new_i, new_j)
                        if not solved:
                            rows[i].remove(num)
                            cols[j].remove(num)
                            boxes[box_id].remove(num)
                            board[i][j]= '.'
        solved = False
        backtrack(0,0)
                                
                    
        
