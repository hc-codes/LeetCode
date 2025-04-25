// Problem: Circular Sentence
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/circular-sentence/
// Date: 2024-11-02

class Solution:
    def isCircularSentence(self, s: str) -> bool:
        if not s:
            return True
        if s[0] != s[-1]:
            return False
        last=""
        for i in range(1,len(s)):
            if s[i]==" ":
                if s[i-1]!=s[i+1]:
                    return False
        return True