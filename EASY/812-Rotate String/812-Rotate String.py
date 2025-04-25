// Problem: Rotate String
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/rotate-string/
// Date: 2024-08-10

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        return (s+s).find(goal)>=0