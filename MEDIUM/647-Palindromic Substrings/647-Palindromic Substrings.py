// Problem: Palindromic Substrings
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/palindromic-substrings/
// Date: 2024-05-12

class Solution:
    def checkPalindrome(self, left,right,s):
        c=0
        while(left>=0 and right<len(s) and s[left]==s[right]):
            c+=1
            left-=1
            right+=1
        return c
    def countSubstrings(self, s: str) -> int:
        oddCount,evenCount=0,0
        res=0
        for i in range(len(s)):
            oddCount+=self.checkPalindrome(i,i,s)
            evenCount+=self.checkPalindrome(i,i+1,s)
        return oddCount+evenCount