// Problem: Divide Two Integers
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/divide-two-integers/
// Date: 2024-10-06

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            c=0
            while dividend >= (divisor << (c+1)):
                c+=1
            res+=1<<c # 2^c calculates the power of 2
            dividend-=(divisor<<c) # n=22; d=3 => n=n-3*2^2 => 22-12 => 10
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)