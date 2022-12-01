class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow = set('aeiouAEIOU')
        sumA = sumB = 0      
        for i in range(len(s)//2):
            # for the first half
            if s[i] in vow:
                sumA += 1
            # len(s)//2+i will go through the second half
            if s[len(s)//2+i] in vow:
                sumB += 1  
        return sumA == sumB
