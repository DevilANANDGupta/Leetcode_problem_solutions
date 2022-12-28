from heapq import *
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = []
        for i in range(len(piles)):
            heappush(maxHeap, -piles[i])

        i = k
        while i > 0:
            temp = heappop(maxHeap)
            x = floor(temp/2)
            heappush(maxHeap,x)
            i -= 1
        return -sum(maxHeap)
