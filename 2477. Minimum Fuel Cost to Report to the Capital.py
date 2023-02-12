from math import ceil
from collections import defaultdict

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        self.ans = 0
        visited = set()
        
        def dfs(i, people = 1):
            visited.add(i)
            for x in graph[i]:
                if x in visited: continue
                people += dfs(x)
            self.ans += (int(ceil(people / seats)) if i else 0)
            return people
        
        dfs(0)
        return self.ans
