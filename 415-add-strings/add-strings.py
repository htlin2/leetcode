class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            return self.addStrings(num2, num1)
        res = []
        carry = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            n1 = int(num1[i])
            n2 = 0 if i >= len(num2) else int(num2[i])
            total = n1 + n2 + carry
            digit = total % 10
            carry = total // 10
            res.append(str(digit))
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])
"""
math
Input: num1 = "11", num2 = "123"
Output: "134"
reverse
add num1 + num2, track carry
add carry back to sum
reverse sum
"""