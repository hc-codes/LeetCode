// Problem: Valid Palindrome
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/valid-palindrome/
// Date: 2024-07-01

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        x=""
        for i in s:
            if((ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57)):
                x+=i
        return x==x[::-1]