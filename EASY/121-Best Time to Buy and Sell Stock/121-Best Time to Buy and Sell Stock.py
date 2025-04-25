// Problem: Best Time to Buy and Sell Stock
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Date: 2024-07-16

class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        buy=nums[0]
        profit=0
        for i in range(1,len(nums)):
            if buy>nums[i]:
                buy=nums[i]
            else:
                profit = max(profit,nums[i]-buy)
            print(nums[i],buy)
        return profit
            