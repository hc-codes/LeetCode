// Problem: Sqrt(x)
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/sqrtx/
// Date: 2023-07-28

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l=2
        r=x
        i=0
        while(True):
            mid = (l+r)//2
            if(mid>x/mid):
                r=mid-1
            else:
                if mid+1>x/(mid+1):
                    return mid
                l=mid+1
