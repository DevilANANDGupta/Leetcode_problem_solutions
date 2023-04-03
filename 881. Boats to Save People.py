class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
    
    # Initialize two pointers
        left, right = 0, len(people) - 1
        
        # Initialize the count of boats
        boats = 0
        
        # Loop until the pointers cross each other
        while left <= right:
            # Check if two people can be accommodated in a single boat
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            
            # Increment the count of boats
            boats += 1
        
        return boats
        
