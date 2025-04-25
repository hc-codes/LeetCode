// Problem: Remove Digit From Number to Maximize Result
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
// Date: 2024-10-27

class Solution:
    def removeDigit(self, n: str, d: str) -> str:
        res=-1
        for i in range(len(n)):
            if n[i]==d:
                res=max(res,int(n[:i]+n[i+1:]))
        return str(res)