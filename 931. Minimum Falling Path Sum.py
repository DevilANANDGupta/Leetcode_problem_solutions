class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if matrix==[] or matrix==[[]]:
        	return 0
        l = len(matrix)
        opt = list(matrix[0])
        for i in range(1, l):
        	cur = [0]*l
        	cur[0] = matrix[i][0] + min([opt[0], opt[1]])
        	for j in range(1, l-1):
        		cur[j] = matrix[i][j] + min([opt[j-1], opt[j], opt[j+1]])
        	cur[-1] = matrix[i][-1] + min(opt[-1], opt[-2])
        	opt = cur
        return min(opt)
