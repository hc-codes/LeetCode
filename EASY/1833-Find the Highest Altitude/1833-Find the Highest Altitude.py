// Problem: Find the Highest Altitude
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/find-the-highest-altitude/
// Date: 2023-06-19

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s=0
        big=0
        for i in gain:
            s=s + i
            if s>big:
                big=s
                
        return big