'''You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

 

Example 1:


Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1
Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0'''

from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)
        
        # [1] first, we list coordinates (x,y) of 1-points in each image
        
        idx1 = [(i//n,i%n) for i in range(n**2) if img1[i//n][i%n]]
        idx2 = [(j//n,j%n) for j in range(n**2) if img2[j//n][j%n]]

        # [2] second, we obtain translation vectors (i1-j1, i2-j2) needed to
        #    overlap each 1-point of img1 with each 1-point of img2, and count
        #    frequencies of these vectors
        
        tr_vecs = Counter((i1-j1, i2-j2) for i1,i2 in idx1 for j1,j2 in idx2)
        
        # [3] translation vector that has been encountered most of the time is
        #    the one that produces an overlap of the maximal number of points
        
        return max(tr_vecs.values()) if tr_vecs else 0
