'''Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Example 2:

Input: nums = [1,2,1]
Output: 0'''




class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        i = n-1
        j = n-3

        while(j>=0):
            if(nums[j]+nums[j+1]>nums[i]):
                return nums[j]+nums[j+1]+nums[i]
            i=i-1
            j=j-1
        return 0
