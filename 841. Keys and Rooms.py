class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        key_queue = []
        visited = [False] * len(rooms)
        for keys in rooms[0]:
            key_queue.append(keys)
        visited[0] = True
        while(key_queue):
            out = key_queue.pop(0)
            if visited[out] != True:
                for keys in rooms[out]:
                    key_queue.append(keys)
                visited[out] = True
        return True if all(visited) else False
