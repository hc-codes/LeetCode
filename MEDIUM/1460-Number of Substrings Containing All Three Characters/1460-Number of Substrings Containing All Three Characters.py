// Problem: Number of Substrings Containing All Three Characters
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
// Date: 2024-11-28

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        d = {'a':0,'b':0,'c':0}
        
        l = 0
        
        for r in range(len(s)):
            d[s[r]] += 1
            
            while d['a'] >= 1 and d['b'] >= 1 and d['c'] >= 1:
                d[s[l]] -= 1
                l += 1
            
                res += len(s) - r
        
        return res