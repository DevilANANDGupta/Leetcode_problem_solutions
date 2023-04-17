class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        kid=len(candies)
        maxcandy=max(candies)
        for i in range(kid):
          
            candies[i]=candies[i]+extraCandies >=maxcandy
            #     i+=1
            #     k.append("true")
            # else:
            #     i+=1
            #     k.append("false")
        return candies
