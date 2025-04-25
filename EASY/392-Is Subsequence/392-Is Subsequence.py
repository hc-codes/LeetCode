// Problem: Is Subsequence
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/is-subsequence/
// Date: 2024-10-13

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        issub=False
        i=0
        j=0
        c=0
        while i<len(s) and j<len(t):
            if t[j]==s[i]:
                i+=1
                c+=1
            j+=1
        print(c)
        return c==len(s)