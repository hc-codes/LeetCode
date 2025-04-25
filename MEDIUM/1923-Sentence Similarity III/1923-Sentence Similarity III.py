// Problem: Sentence Similarity III
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/sentence-similarity-iii/
// Date: 2024-10-06

class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            s1,s2=s2,s1
        s1=s1.split()
        s2=s2.split()
        while(s1):
            if(s1[0]==s2[0]):
                s1.pop(0)
                s2.pop(0)
            elif(s1[-1]==s2[-1]):
                s1.pop()
                s2.pop()
            else:
                return False
        return True
                