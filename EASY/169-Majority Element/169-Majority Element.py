// Problem: Majority Element
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/majority-element/
// Date: 2024-09-25

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        vote = 1
        for i in nums[1:len(nums)+1]:
            if vote==0:
                major=i
                vote=1
                continue
            if major==i:
                vote+=1
            else:
                vote-=1
        return major
                