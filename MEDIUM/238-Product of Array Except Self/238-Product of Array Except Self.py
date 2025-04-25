// Problem: Product of Array Except Self
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/product-of-array-except-self/
// Date: 2024-05-03

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        right=[1]*len(nums)
        p=1
        for i in range(len(nums)-1):
            p=p*nums[i]
            left[i+1]=p
        j=len(nums)-1
        p=1
        while(j>0):
            p=p*nums[j]
            right[j-1]=p
            j-=1
        print(left)
        print(right)
        for i in range(len(left)):
            left[i]=left[i]*right[i]
        return left
            