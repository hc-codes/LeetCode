// Problem: Climbing Stairs
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/climbing-stairs/
// Date: 2024-07-16

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        a=1
        b=2
        c=0
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return c
        