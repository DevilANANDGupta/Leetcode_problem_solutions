'''When we write code of Binary search of an array is maximum number of lines of code are there so to avoid and minimise the number of
code we use direct built-in python module for binary search ie. bisect  
& If target already exists, returns the index of where it is'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
