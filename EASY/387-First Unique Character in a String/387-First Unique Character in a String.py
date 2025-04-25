// Problem: First Unique Character in a String
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/first-unique-character-in-a-string/
// Date: 2024-09-29

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==1:
            return 0
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1