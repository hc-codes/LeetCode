// Problem: The Two Sneaky Numbers of Digitville
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
// Date: 2024-09-22

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if nums.count(nums[i])>1:
                res.append(nums[i])
        return set(res)