class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod, res, stack = 1000000007, 0, []
        
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                idx = stack.pop()
                l, r = stack[-1] if stack else -1, i
                res += (r-idx) * (idx-l) * arr[idx]
                res %= mod
            stack.append(i)
            
        while stack:
            idx = stack.pop()
            l, r = stack[-1] if stack else -1, len(arr)
            res += (r-idx) * (idx-l) * arr[idx]
            res %= mod
            
        return res
