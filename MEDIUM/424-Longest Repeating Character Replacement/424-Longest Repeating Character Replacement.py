// Problem: Longest Repeating Character Replacement
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/longest-repeating-character-replacement/
// Date: 2024-11-23

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        cur_max = 0
        l = 0
        d = defaultdict(int)
        for r in range(len(s)):
            d[s[r]] += 1
            cur_max = max(cur_max, d[s[r]])
            
            # window - max gives replaced count
            if r - l + 1 - cur_max > k:
                d[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
        return res