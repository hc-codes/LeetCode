// Problem: Find Words Containing Character
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/find-words-containing-character/
// Date: 2024-08-13

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res=[]
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
                
        return res