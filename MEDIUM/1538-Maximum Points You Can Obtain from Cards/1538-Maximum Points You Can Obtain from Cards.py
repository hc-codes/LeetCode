// Problem: Maximum Points You Can Obtain from Cards
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
// Date: 2024-11-28

class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        res = 0
        lsum = sum(nums[0:k])
        rsum = 0
        
        res = max(lsum + rsum, res)
        l = k-1
        r = len(nums) - 1
        while l >= 0 and r + k >= len(nums):
            # print(lsum, rsum)
            lsum -= nums[l]
            l -= 1
            
            rsum += nums[r]
            r -= 1
            
            res = max(res, lsum + rsum)
        return res