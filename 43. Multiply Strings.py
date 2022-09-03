'''Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        l1, l2 = len(num1), len(num2)
        l3 = l1 + l2
        results = [0 for i in range(l3)]
        
        
        for i in range(l1 - 1, -1, -1):
            carry = 0
            for j in range(l2 - 1, -1, -1):
                results[i + j + 1] += carry + int(num1[i]) * int(num2[j])
                
                carry = results[i + j + 1] // 10
                results[i + j + 1] %= 10
                
            results[i] = carry
            
            
        i = 0 
        while i < l3 and results[i] == 0:
            i += 1
            
        results = results[i:]
        
        return '0' if not results else ''.join(str(i) for i in results)
    
