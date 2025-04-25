// Problem: Single Number
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/single-number/
// Date: 2024-07-15

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            a=a^i
        return a