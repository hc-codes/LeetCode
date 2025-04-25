// Problem: Running Sum of 1d Array
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/running-sum-of-1d-array/
// Date: 2023-04-01

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        sum=0
        for i in nums:
            sum=sum+i
            res.append(sum)
        return res