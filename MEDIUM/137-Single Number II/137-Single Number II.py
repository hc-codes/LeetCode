// Problem: Single Number II
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/single-number-ii/
// Date: 2024-07-20

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=nums[0]
        for i in range(1,len(nums)):
            if nums.count(nums[i])==1:
                s=nums[i]
             
        return s