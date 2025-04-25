// Problem: Next Permutation
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/next-permutation/
// Date: 2024-07-24

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(i,j):
            while(i<j):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        idx=-1
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<nums[i+1]):
                idx=i
                break
        if idx==-1:
            rev(0,len(nums)-1)
            return
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]>nums[idx]):
                nums[i],nums[idx]=nums[idx],nums[i]
                break
        rev(idx+1,len(nums)-1)