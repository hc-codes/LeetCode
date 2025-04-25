// Problem: Richest Customer Wealth
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/richest-customer-wealth/
// Date: 2023-04-01

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        big=0;
        s=0
        for i in accounts:
            s=sum(i)
            if s> big:
                big=s
      
        return big