// Problem: Take K of Each Character From Left and Right
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/
// Date: 2024-11-20

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        res = len(s)
        left = 0
        right = 0
        d = Counter(s)
        if min(d.values()) < k or len(set(s)) < 3 and k>0:
            return -1
        
        for right in range(len(s)):
            d[s[right]] -= 1
            
            while min(d.values()) < k:
                d[s[left]] += 1 
                left = left + 1
            
            res = min(res, len(s) - (right - left + 1))
        return res
                    