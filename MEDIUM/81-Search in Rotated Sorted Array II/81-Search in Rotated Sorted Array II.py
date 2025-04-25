// Problem: Search in Rotated Sorted Array II
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
// Date: 2024-07-26

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pvt=-1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                pvt=i-1
                break
        def BS(nums,l,r):
            while(l<=r):
                m=(l+r)//2
                if (nums[m]==target):
                    return m
                elif nums[m]>target:
                    r=m-1
                else:
                    l=m+1
            return -1
        ans = -1
        ans = BS(nums,0,pvt)
        if ans==-1:
            ans = BS(nums,pvt+1,len(nums)-1)
        return ans!=-1