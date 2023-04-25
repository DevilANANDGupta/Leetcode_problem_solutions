import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.pq = []
        for i in range(1, 1001):
            heapq.heappush(self.pq, i)

    def popSmallest(self):
        if self.pq:
            return heapq.heappop(self.pq)
        return -1

    def addBack(self, num):
        if num not in self.pq:
            heapq.heappush(self.pq, num)
