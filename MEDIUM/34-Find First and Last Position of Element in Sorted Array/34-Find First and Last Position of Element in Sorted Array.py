// Problem: Find First and Last Position of Element in Sorted Array
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
// Date: 2024-07-26

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        s=e=-1
        r=len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if(target>nums[m]):
                l=m+1
            elif target<nums[m]:
                r=m-1
            else:
                mm=m
                while(m>=l and nums[m]==target):
                    m-=1
                s=m+1
                while(mm<=r and nums[mm]==target):
                    mm+=1
                e=mm-1
                break
        return [s,e]