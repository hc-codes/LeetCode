// Problem: Pow(x, n)
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/powx-n/
// Date: 2024-11-09

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n<0:
            x=1/x
            n=n*-1
        def pow(x,n):
            if n==0:
                return 1
            if n==1:
                return x
            if n%2==0:
                return pow(x*x,n//2)
            return x*pow(x,n-1)
        return pow(x,n)