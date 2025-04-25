// Problem: Palindrome Number
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/palindrome-number/
// Date: 2024-09-28

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        res=0
        n=x
        while(x>0):
            res=res*10 + x%10
            x=x//10
        return n==res