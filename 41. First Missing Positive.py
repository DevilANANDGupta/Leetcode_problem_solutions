'''Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.'''


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                
                if nums[val - 1] > 0:
                    nums[val -1] *= -1
                elif nums[val -1] == 0:
                    nums[val-1] = -1 *(len(nums)+ 1)
        for i in range(1, len(nums) +1):
            if nums[i-1] >= 0:
                return i 
        return len(nums) +1
        
        
