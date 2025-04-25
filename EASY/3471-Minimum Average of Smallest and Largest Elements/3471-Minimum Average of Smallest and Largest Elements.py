// Problem: Minimum Average of Smallest and Largest Elements
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
// Date: 2024-09-13

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        mn_avg=max(nums)
        while nums:
            mx=max(nums)
            mn=min(nums)
            avg=(mx+mn)/2
            mn_avg=min(mn_avg,avg)
            nums.remove(mx)
            nums.remove(mn)
        return mn_avg
            
            