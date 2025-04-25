// Problem: Ransom Note
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/ransom-note/
// Date: 2024-06-28

class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        d={}
        for i in b:
            if d and i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in a:
            if d and i not in d:
                return False
            if(a.count(i)>d[i]):
                return False
        return True