// Problem: Length of Last Word
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/length-of-last-word/
// Date: 2023-07-27

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])