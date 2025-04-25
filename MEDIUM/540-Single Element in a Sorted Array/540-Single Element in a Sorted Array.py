// Problem: Single Element in a Sorted Array
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/single-element-in-a-sorted-array/
// Date: 2024-07-28

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            m=l+(r-l)//2
            a=m%2==0 and nums[m]==nums[m-1]
            b=m%2!=0 and nums[m]==nums[m+1]
            if a or b:
                r=m-1
            else:
                l=m+1
        return nums[l-1]