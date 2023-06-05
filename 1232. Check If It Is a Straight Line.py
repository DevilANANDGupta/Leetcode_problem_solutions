class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<=2:
            return True
        x0,y0=coordinates[0]
        x1,y1=coordinates[1]
        if x1-x0 == 0:
            slope = float('inf')
        else:
            slope=(y1-y0)/(x1-x0)
        for i in range(2, len(coordinates)):
            xi,yi=coordinates[i]
            if xi - x0 == 0:
                if slope != float('inf'):
                    return False
            else:
                if slope != (yi-y0)/(xi-x0):
                    return False
        return True
