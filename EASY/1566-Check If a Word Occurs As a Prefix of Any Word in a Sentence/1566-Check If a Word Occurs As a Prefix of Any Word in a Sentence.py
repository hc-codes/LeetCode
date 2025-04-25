// Problem: Check If a Word Occurs As a Prefix of Any Word in a Sentence
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
// Date: 2024-12-02

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        res = -1
        c = 1
        for i in words:
            if i.startswith(searchWord):
                return c
            c += 1
        return res