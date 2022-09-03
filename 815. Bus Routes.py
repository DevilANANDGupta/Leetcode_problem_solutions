'''You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1'''

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stoptoRoutes = {}
        for route in range(len(routes)):
            for stop in routes[route]:
                if stop not in stoptoRoutes:
                    stoptoRoutes[stop] = set()
                stoptoRoutes[stop].add(route)
        visited_routes, visited_stops = set(), set()
        queue = [(source, 0)]
        while len(queue) != 0:
            currStop , busesToken = queue.pop(0)
            if currStop not in visited_stops:
                if currStop == target:
                    return busesToken
                visited_stops.add(currStop)
                for connectedRoute in stoptoRoutes[currStop]:
                    if connectedRoute not in visited_routes:
                        for connectedStop in routes[connectedRoute]:
                            if connectedStop not in visited_stops:
                                queue.append((connectedStop, busesToken +1))
                        visited_routes.add(connectedRoute)
        return -1
                    
