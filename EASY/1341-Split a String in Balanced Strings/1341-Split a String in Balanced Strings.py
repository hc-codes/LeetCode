// Problem: Split a String in Balanced Strings
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/split-a-string-in-balanced-strings/
// Date: 2024-08-17

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        i=0
        lc,rc=0,0
        res=0
        while(i<len(s)):
            # if (s[i]=="L" and s[j]=="R") or (s[i]=="R" and s[j]=="L") or (lc==rc):
            #     res+=1
            #     lc=rc=0
            # elif s[i]
            if s[i]=="R":
                rc+=1
            elif s[i]=="L":
                lc+=1
            if lc==rc:
                res+=1
            i+=1
        return res
                