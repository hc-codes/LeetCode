// Problem: Remove Duplicates from Sorted Array
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
// Date: 2024-07-17

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=0
        i=1
        while(i<len(nums)):
            if(nums[i]==nums[i-1]):
                c+=1
            else:
                nums[i-c]=nums[i]
            i+=1
        return len(nums)-c