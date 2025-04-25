// Problem: Largest Odd Number in String
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/largest-odd-number-in-string/
// Date: 2024-08-09

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                return num[:i+1]
        return ""