class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)  # sort satisfaction in decreasing order
        curr_sum = max_sum = 0
        for s in satisfaction:
            curr_sum += s
            max_sum += curr_sum if curr_sum > 0 else 0
        return max_sum
