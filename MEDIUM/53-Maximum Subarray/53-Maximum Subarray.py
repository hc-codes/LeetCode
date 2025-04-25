// Problem: Maximum Subarray
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/maximum-subarray/
// Date: 2024-09-25

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        big=nums[0]
        csum=0
        for i in range(len(nums)):
            csum=csum+nums[i]
            big=max(big,csum)
            if csum<0:
                csum=0
        return big