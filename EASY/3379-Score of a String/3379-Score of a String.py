// Problem: Score of a String
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/score-of-a-string/
// Date: 2024-08-11

class Solution:
    def scoreOfString(self, s: str) -> int:
        ss=0
        for i in range(1,len(s)):
            ss+=abs(ord(s[i])-ord(s[i-1]))
        return ss