// Problem: Shuffle String
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/shuffle-string/
// Date: 2024-08-19

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        if not s:
            return ""
        res=[0]*len(s)
        c=0
        for i in range(len(s)):
            
            res[int(indices[i])]=s[c]
            c+=1
        return "".join(res)