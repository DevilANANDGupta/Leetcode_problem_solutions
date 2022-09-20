'''Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5'''

# class Solution:
#   def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#     ans = 0
#     dp = [0] * (len(nums2) + 1)

#     for a in reversed(nums1):
#       for j, b in enumerate(nums2):
#         dp[j] = dp[j + 1] + 1 if a == b else 0
#         ans = max(ans, dp[j])

#     return ans
# class Solution:
#   def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#     m = len(nums1)
#     n = len(nums2)
#     ans = 0
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
#     for i in reversed(range(m)):
#       for j in reversed(range(n)):
#         if nums1[i] == nums2[j]:
#           dp[i][j] = dp[i + 1][j + 1] + 1
#           ans = max(ans, dp[i][j])

#     return ans
# class Solution:
    
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#         n, m = len(nums1), len(nums2)
#         # dp[i][j] means the length of repeated subarray of nums1[:i] and nums2[:j]
#         dp = [[0] * (m + 1) for _ in range(n + 1)]
#         ans = 0
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 # if both character is same
#                 if nums1[i - 1] == nums2[j - 1]:
#                     # then we add 1 to the previous state, which is dp[i - 1][j - 1]
#                     # in other word, we extend the repeated subarray by 1
#                     # e.g. a = [1], b = [1], length of repeated array is 1
#                     #      a = [1,2], b = [1,2], length of repeated array is the previous result + 1 = 2
#                     dp[i][j] = dp[i - 1][j - 1] + 1
#                     # record the max ans here
#                     ans = max(ans, dp[i][j])
#                 # else:
#                     # if you are looking for longest common sequence,
#                     # then you put dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]); here
#                     # however, this problem is looking for subarray,
#                     # since both character is not equal, which means we need to break it here
#                     # hence, set dp[i][j] to 0
#         return ans


#faster than other method

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        
        def ok(k):
            s = set(tuple(nums1[i : i + k]) for i in range(N - k + 1))
            return any(tuple(nums2[i : i + k]) in s for i in range(M - k + 1))
        l, r = 0, min(N, M)
        while l < r:
            m = (l + r + 1) // 2
            if ok(m): 
                l = m
            else:
                r = m - 1
        return l
