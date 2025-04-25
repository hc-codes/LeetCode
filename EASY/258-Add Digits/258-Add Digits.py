// Problem: Add Digits
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/add-digits/
// Date: 2024-07-17

class Solution:
    def addDigits(self, num: int) -> int:
        if num<=9:
            return num
        s=0
        while(num>0 or (s>9 or s==0)):
            r=num%10
            s=s+r
            num=num//10
            if(num==0 and s>9):
                num=s
                s=0
        return s