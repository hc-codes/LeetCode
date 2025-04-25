// Problem: Find Numbers with Even Number of Digits
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
// Date: 2023-06-16

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        for i in nums:
            a = str(i)
            if(len(a)%2==0):
                s+=1
        return s
