'''In this problem we have to find pivot index of an array which is given in question , if you don't know about pivot index  . read it carefully 
Pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left therefor i initiate the value of pre is 0.'''
class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    summ = sum(nums)
    pre = 0

    for i, num in enumerate(nums):
      if pre == summ - pre - num:
        return i
      pre += num

    return -1
