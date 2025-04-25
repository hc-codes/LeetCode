// Problem: Missing Number
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/missing-number/
// Date: 2024-07-06

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(len(nums)):
        s=0
        n=len(nums)
        for i in nums:
            s+=i
        return (n*(n+1)//2)-s
            