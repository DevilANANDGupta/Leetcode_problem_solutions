
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if len(stones)
    

    # def lastStoneWeight(stones):
        heap = [-stone for stone in stones]  # Negate the stones to create a max heap
        heapq.heapify(heap)
        
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, x - y)
                
        return -heap[0] if heap else 0
