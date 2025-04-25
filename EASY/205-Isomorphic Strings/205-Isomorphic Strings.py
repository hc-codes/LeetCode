// Problem: Isomorphic Strings
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/isomorphic-strings/
// Date: 2024-08-10

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            a.append(s.index(i))
        for i in t:
            b.append(t.index(i))
        return a==b