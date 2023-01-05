class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x: x[1])
        first_end = points[0][1]
        arrow = 1
        for i in range(1,len(points)):
            start, end = points[i]
            if start > first_end:
                arrow+=1
                first_end = end
        return arrow
