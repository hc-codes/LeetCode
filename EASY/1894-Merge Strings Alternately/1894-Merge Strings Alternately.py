// Problem: Merge Strings Alternately
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/merge-strings-alternately/
// Date: 2024-01-06

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=""
        i=0
        j=0
        toggle = True
        while(i<len(word1) or j<len(word2)):
            if(i>=len(word1)):
                toggle=False
            if(j>=len(word2)):
                toggle=True
            if(toggle):
                word3=word3+word1[i]
                i+=1
            else:
                word3+=word2[j]
                j+=1
            toggle = not toggle
        return word3