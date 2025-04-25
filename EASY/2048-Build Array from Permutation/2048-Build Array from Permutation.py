// Problem: Build Array from Permutation
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/build-array-from-permutation/
// Date: 2024-09-01

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        ans=[0]*len(nums)
        for i in range(len(nums)):
            ans[i]=nums[nums[i]]
        return ans