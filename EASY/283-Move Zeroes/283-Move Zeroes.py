// Problem: Move Zeroes
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/move-zeroes/
// Date: 2024-09-25

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        i=1
        while(i<len(nums) and zero <len(nums)):
            if(nums[i]!=0 and nums[zero]==0):
                nums[zero],nums[i]=nums[i],nums[zero]
                zero+=1
                i+=1
                continue
            if(nums[zero]!=0):
                zero+=1
            i+=1