class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        min_sum, min_index, total = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if min_sum > total:
                min_sum, min_index = total, i + 1
        return -1 if total < 0 else min_index
