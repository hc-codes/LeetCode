// Problem: Next Greater Element I
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/next-greater-element-i/
// Date: 2024-09-06

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        mapping = {}
        
        for n in nums2:
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n
            stack.append(n)
            
        while stack:
            mapping[stack.pop()] = -1
            
        for n in nums1:
            res.append(mapping[n])

        return res