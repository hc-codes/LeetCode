// Problem: Reverse Integer
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/reverse-integer/
// Date: 2024-06-28

class Solution:
    def reverse(self, x: int) -> int:
        mul=1
        if(x<0):
            x=x*-1
            mul=-1
        res=0
        while(x>0):
            res=res*10+x%10
            x=x//10
        if(res > (2**31)-1 or res < -(2**31)):
            return 0
        return res*mul