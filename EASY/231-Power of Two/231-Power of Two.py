// Problem: Power of Two
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/power-of-two/
// Date: 2024-10-03

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n%2!=0 or n==0:
            return False
        return self.isPowerOfTwo(n/2)