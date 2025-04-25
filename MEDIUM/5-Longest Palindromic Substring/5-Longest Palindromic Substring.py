// Problem: Longest Palindromic Substring
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/longest-palindromic-substring/
// Date: 2024-05-11

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            c=0
            l=r=i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
                c+=1
            if(len(s[l+1:r])>len(res)):
                res=s[l+1:r]
            l,r,c=i,i+1,0
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
                c+=1
            if(len(s[l+1:r])>len(res)):
                res=s[l+1:r]
        return res