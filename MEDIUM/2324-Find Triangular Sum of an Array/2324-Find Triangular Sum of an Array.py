// Problem: Find Triangular Sum of an Array
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/find-triangular-sum-of-an-array/
// Date: 2024-07-23

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        ans=0
        ncr=1
        n=len(nums)-1
        for i in range(len(nums)):
            ans+=(ncr*nums[i])
            ncr=(ncr*(n-i))//(i+1)
        return ans%10