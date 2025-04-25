// Problem: Reverse Vowels of a String
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/reverse-vowels-of-a-string/
// Date: 2024-10-13

class Solution:
    def reverseVowels(self, s: str) -> str:
        v=['a','e','i','o','u']
        vl=[]
        for i in range(len(s)):
            # print(s[i] in v)
            if s[i].lower() in v:
                vl.append(s[i])
        print(vl)
        # vl=[i for i in vl[::-1]]
        print(vl)
        res=""
        for i in range(len(s)):
            if s[i].lower() in v:
                res+=vl.pop()
            else:
                res+=s[i]
        return res