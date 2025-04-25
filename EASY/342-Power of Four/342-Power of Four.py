// Problem: Power of Four
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/power-of-four/
// Date: 2024-10-03

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n==0 or n%4!=0:
            return False
        return self.isPowerOfFour(n/4)