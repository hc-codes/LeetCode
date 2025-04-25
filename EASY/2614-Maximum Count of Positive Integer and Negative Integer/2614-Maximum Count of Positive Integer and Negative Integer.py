// Problem: Maximum Count of Positive Integer and Negative Integer
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
// Date: 2024-10-26

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        n,p=0,0
        while(l<=r):
            m=l+(r-l)//2
            if nums[m]<0:
                p=m+1
                l=m+1
            else:
                r=m-1
        l=0
        r=len(nums)-1
        while(l<=r):
            m=l+(r-l)//2
            if nums[m]>0:
                n=len(nums)-m
                r=m-1
            else:
                l=m+1
        return max(n,p)
        