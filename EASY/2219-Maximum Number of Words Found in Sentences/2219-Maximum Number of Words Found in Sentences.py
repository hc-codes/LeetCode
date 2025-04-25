// Problem: Maximum Number of Words Found in Sentences
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
// Date: 2024-08-17

class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        ml=0
        for i in s:
            cs=list(i.split(" "))
            ml=max(ml,len(cs))
        return ml
        