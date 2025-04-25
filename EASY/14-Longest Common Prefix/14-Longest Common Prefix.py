// Problem: Longest Common Prefix
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/longest-common-prefix/
// Date: 2024-08-10

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=strs[0]
        longest=""
        for i in range(len(prefix)):
            letter=prefix[i]
            for nextword in strs[1:]:
                if i>=len(nextword) or nextword[i]!=letter:
                    return longest
            longest+=letter
        return longest