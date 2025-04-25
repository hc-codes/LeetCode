// Problem: Repeated Substring Pattern
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/repeated-substring-pattern/
// Date: 2023-12-02

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        cs=s+s
        cs=cs[1:len(cs)-1]
        print(cs)
        print(s)
        if(s in cs):
            return True
        return False
            