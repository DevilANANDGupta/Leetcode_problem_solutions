class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
    # def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] - mid > k: hi = mid
            else: lo = mid + 1
        return lo + k
