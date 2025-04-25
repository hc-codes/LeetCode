// Problem: Check if Array Is Sorted and Rotated
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
// Date: 2024-09-25

class Solution:
    def check(self, nums: List[int]) -> bool:
        count=0
        for i in range(len(nums)):
            if(nums[i]>nums[(i+1)%len(nums)]):
                count+=1
        return count<=1