// Problem: Valid Parentheses
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/valid-parentheses/
// Date: 2023-07-22

class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2 != 0):
            return False
        brackets = {"(":")", "[": "]", "{": "}"}
        opened = []
        for i in range(0, len(s)):
            if s[i] in brackets.keys():
                opened.append(s[i])
                continue
            if not opened:
                return False
            if brackets[opened[-1]] == s[i]:
                opened.pop()
            else:
                return False
        return opened == []
                