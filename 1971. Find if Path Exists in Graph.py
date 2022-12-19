class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        # make graph
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited=[]
        route=set([source])
        while route:
            node=route.pop()
            if node==destination:
                return True
            # mark visited node
            visited.append(node)
            for d in graph[node]:
                if d not in visited:
                    route.add(d)
        return False
