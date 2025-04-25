// Problem: Count the Number of Consistent Strings
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/count-the-number-of-consistent-strings/
// Date: 2024-09-14

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        c=0
        for word in words:
            if all(char in allowed for char in word):
                c+=1
        return c