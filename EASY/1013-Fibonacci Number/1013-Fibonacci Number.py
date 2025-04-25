// Problem: Fibonacci Number
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/fibonacci-number/
// Date: 2024-07-01

class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        if(n==1):
            return 1
        return self.fib(n-1)+self.fib(n-2)