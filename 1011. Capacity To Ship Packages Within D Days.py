class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)

        # binary search for the minimum weight capacity that can ship all packages in days days
        while lo < hi:
            mid = (lo + hi) // 2
            curr_weight = 0
            curr_days = 1

            for weight in weights:
                if curr_weight + weight > mid:
                    # need to start a new day with a new ship
                    curr_weight = weight
                    curr_days += 1
                else:
                    # can continue to load packages on the same ship
                    curr_weight += weight

            if curr_days > days:
                # if it takes more than days days to ship all packages, we need to increase the weight capacity
                lo = mid + 1
            else:
                # if it takes less than or equal to days days to ship all packages, we can try reducing the weight capacity
                hi = mid

        return lo
