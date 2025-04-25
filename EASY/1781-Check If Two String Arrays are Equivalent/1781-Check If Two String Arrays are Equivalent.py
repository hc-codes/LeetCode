// Problem: Check If Two String Arrays are Equivalent
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
// Date: 2024-08-17

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=""
        w2=""
        for i in word1:
            w1+=i
        for i in word2:
            w2+=i
        return w1==w2