// Problem: Add Binary
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/add-binary/
// Date: 2023-07-27

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        carry=0
        result=''
        while a or b or carry:
            if a:
                carry +=int(a.pop())
            if b:
                carry +=int(b.pop())
            result +=str(carry%2)
            carry=carry//2
        return result[::-1]