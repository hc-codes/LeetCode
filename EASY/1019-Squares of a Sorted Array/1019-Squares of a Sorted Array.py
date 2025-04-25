// Problem: Squares of a Sorted Array
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/squares-of-a-sorted-array/
// Date: 2023-06-16

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in nums:
            a.append(i**2)
        a.sort()
        return a