'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.'''


# first method -

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)+1):
            if i not in nums:
                
                return i
              
              
              
# second method
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range (len(nums)+1):
            if i not in nums:
                return i
# third method by xor function to reduce time complexity
# xor function work as if same number is formed then it will be zero if different number will form then it will not zero thats why we return that value
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    #initialize value
        x1=0
        x2=0
        for i in range(len(nums)+1):
            x1=x1^i
        for i in range(len(nums)):
            x2=x2^nums[i]
        return x1^x2
            
        
        
