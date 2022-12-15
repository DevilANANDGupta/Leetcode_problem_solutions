class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1) ]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    res[i+1][j+1] = res[i][j] + 1
                else:
                    res[i+1][j+1] = max(res[i+1][j], res[i][j+1])
        return max((max(row) for row in res))
