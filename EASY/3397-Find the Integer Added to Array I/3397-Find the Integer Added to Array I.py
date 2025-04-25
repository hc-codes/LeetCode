// Problem: Find the Integer Added to Array I
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/find-the-integer-added-to-array-i/
// Date: 2024-05-04

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        dif=nums2[0]-nums1[0]
        return dif
            