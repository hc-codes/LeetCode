// Problem: Find Peak Element
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/find-peak-element/
// Date: 2025-03-24

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        n = len(nums)
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        l = 1
        r = n - 2
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1] and nums[m] > nums[m - 1]:
                return m
            elif nums[m] >= nums[m - 1]:
                l = m + 1
            else:
                r = m - 1
        return -1
