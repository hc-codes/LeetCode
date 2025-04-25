// Problem: Max Consecutive Ones III
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/max-consecutive-ones-iii/
// Date: 2024-11-28

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        flips = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                flips += 1
            
            if flips > k:
                if nums[l] == 0:
                    flips -= 1
                l += 1
            if flips <= k:
                res = max(res, r - l + 1)
        return res
        