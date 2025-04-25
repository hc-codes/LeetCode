// Problem: Max Consecutive Ones
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/max-consecutive-ones/
// Date: 2024-07-15

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                continue
            else:
                m=max(c,m)
                c=0
        return max(c,m)