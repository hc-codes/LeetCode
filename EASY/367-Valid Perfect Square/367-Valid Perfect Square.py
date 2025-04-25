// Problem: Valid Perfect Square
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/valid-perfect-square/
// Date: 2024-08-01

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=num
        while(l<=r):
            m=(l+r)//2
            sq=m**2
            if sq==num:
                return True
            elif sq>num:
                r=m-1
            else:
                l=m+1
        return False