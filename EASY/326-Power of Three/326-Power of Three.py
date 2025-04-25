// Problem: Power of Three
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/power-of-three/
// Date: 2024-10-03

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 1,3,9,27,81,243,729,2187,
        # 5,7,11,13,15,17,21
        if n==1:
            return True
        if n%3!=0 or n==0:
            return False
        return self.isPowerOfThree(n/3)