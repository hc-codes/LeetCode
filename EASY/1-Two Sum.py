// Problem: Two Sum
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/two-sum/
// Date: 2025-04-24

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target-nums[i]]=i
            elif nums[i] in d:
                return [d[nums[i]],i]
        return [-1,-1]