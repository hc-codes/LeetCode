// Problem: Rotate Array
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/rotate-array/
// Date: 2024-10-20

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        nums[:] = nums[n-k:]+nums[:n-k]