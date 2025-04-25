// Problem: Search Insert Position
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/search-insert-position/
// Date: 2024-07-25

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        # print(l,mid,r)
        return l