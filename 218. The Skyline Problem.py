'''A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.'''



class Solution:
  def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    n = len(buildings)
    if n == 0:
      return []
    if n == 1:
      left, right, height = buildings[0]
      return [[left, height], [right, 0]]

    left = self.getSkyline(buildings[:n // 2])
    right = self.getSkyline(buildings[n // 2:])
    return self._merge(left, right)

  def _merge(self, left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
    ans = []
    i = 0  # left's index
    j = 0  # right's index
    leftY = 0
    rightY = 0

    while i < len(left) and j < len(right):
      # choose the powith smaller x
      if left[i][0] < right[j][0]:
        leftY = left[i][1]  # update the ongoing leftY
        self._addPoint(ans, left[i][0], max(left[i][1], rightY))
        i += 1
      else:
        rightY = right[j][1]  # update the ongoing rightY
        self._addPoint(ans, right[j][0], max(right[j][1], leftY))
        j += 1

    while i < len(left):
      self._addPoint(ans, left[i][0], left[i][1])
      i += 1

    while j < len(right):
      self._addPoint(ans, right[j][0], right[j][1])
      j += 1

    return ans

  def _addPoint(self, ans: List[List[int]], x: int, y: int) -> None:
    if ans and ans[-1][0] == x:
      ans[-1][1] = y
      return
    if ans and ans[-1][1] == y:
      return
    ans.append([x, y])
