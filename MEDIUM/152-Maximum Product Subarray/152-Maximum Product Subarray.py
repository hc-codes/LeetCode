// Problem: Maximum Product Subarray
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/maximum-product-subarray/
// Date: 2024-09-07

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        minprod=nums[0]
        maxprod=nums[0]
        big=nums[0]
        for i in range(1,len(nums)):
            if(nums[i]<0):
                minprod,maxprod=maxprod,minprod
            minprod=min(nums[i],nums[i]*minprod)
            maxprod=max(nums[i],nums[i]*maxprod)
            big=max(maxprod,big)
        return big