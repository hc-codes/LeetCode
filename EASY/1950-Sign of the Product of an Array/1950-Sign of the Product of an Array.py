// Problem: Sign of the Product of an Array
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/sign-of-the-product-of-an-array/
// Date: 2023-12-13

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        neg=0
        for i in nums:
            if i<0:
                neg+=1
        if(neg%2==0):
            return 1
        return -1