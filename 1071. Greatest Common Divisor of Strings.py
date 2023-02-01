class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s=""
        ans=""
        for i in range(len(str1)):
            s+=str1[i]
            if len(str1)%(i+1)==0 and len(str2)%(i+1)==0:
                if s*(len(str1)//(i+1))==str1 and s*(len(str2)//(i+1))==str2:
                    ans=s
        return ans
