'''You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.'''



class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []
        for eff, spd in zip(efficiency , speed):
            eng.append([eff, spd])
        eng.sort(reverse = True)
        res, speed = 0 , 0 
        minHeap=[]
        for eff, spd in eng:
            if len(minHeap) == k:
               speed -= heapq.heappop(minHeap)
            speed += spd
            heapq.heappush(minHeap, spd)
            res = max(res, eff* speed)
        return res % (10** 9 + 7)
            
        
