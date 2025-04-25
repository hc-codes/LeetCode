// Problem: Reverse Words in a String
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/reverse-words-in-a-string/
// Date: 2024-08-15

class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        s=s.strip()
        i=len(s)-1
        j=len(s)
        while(i>=0):
            if s[i]!=" ":
                i-=1
            elif s[i]==" " and s[i+1]!=" ":
                res+=s[i+1:j]+s[i]
                j=i
                i-=1
            else:
                i-=1
                j-=1
        res=res+s[i+1:j]
        return res