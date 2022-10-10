class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        else:
            if len(palindrome) < 2:
                return ''
            return palindrome[:-1] + 'b'
