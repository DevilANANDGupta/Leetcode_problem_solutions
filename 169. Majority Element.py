'''
Easy

11271

370

Add to List

Share
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?'''


# This question was ask in visa and microsoft 


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() #time complexity is n(logn)
        count = 0
        n=len(nums)//2 #majority condition
        num= nums[0]
        for i in range(len(nums)):
            
            if num==nums[i]:
                count+=1
            
            
            else:
                count=1
            if count>n:
                return num
            num = nums[i]
