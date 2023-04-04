class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        result = 0
        for c in s:
            if c not in seen:
                seen.add(c)
            else:
                seen = set(c)
                result += 1
        return result + 1
