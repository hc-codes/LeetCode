// Problem: Longest Substring Without Repeating Characters
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Date: 2024-12-23

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq, leftIndex, big = Counter(), 0, 0
        for i in range(len(s)):
            freq[s[i]]+=1
            while(freq[s[i]]>=2):
                freq[s[leftIndex]]-=1
                leftIndex+=1
            big = max(big, i-leftIndex+1)
        return big