class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # def count_zero_subarrays(nums):
        count = 0
        length = len(nums)
        i = 0
        
        while i < length:
            if nums[i] == 0:
                j = i + 1
                while j < length and nums[j] == 0:
                    j += 1
                subarray_length = j - i
                count += (subarray_length * (subarray_length + 1)) // 2
                i = j
            else:
                i += 1
        
        return count
