// Problem: Find Minimum in Rotated Sorted Array
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// Date: 2024-10-23

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = l + (r - l) // 2
            if nums[l] < nums[r]:
                return nums[l]
            
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m

        return nums[l]