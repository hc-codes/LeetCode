// Problem: Truncate Sentence
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/truncate-sentence/
// Date: 2024-08-17

class Solution:
    def truncateSentence(self, ss: str, k: int) -> str:
        s=ss.split(" ")
        if len(s)==k:
            return ss
        print(s)
        res=""
        for i in range(len(s)):
            if i==k:
                return res[0:len(res)-1]
            res+=s[i]+" "
            print(res)
        return ""