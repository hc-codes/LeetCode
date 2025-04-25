// Problem: Reverse Prefix of Word
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/reverse-prefix-of-word/
// Date: 2024-08-17

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx=word.find(ch)
        print(word[0:idx+1])
        if idx<0:
            return word
        s=word[0:idx+1]
        return s[::-1]+word[idx+1:]