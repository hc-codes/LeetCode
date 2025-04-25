// Problem: Uncommon Words from Two Sentences
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/uncommon-words-from-two-sentences/
// Date: 2024-09-20

class Solution:
    def uncommonFromSentences(self, ss1: str, ss2: str) -> List[str]:
        d={}
        s1=list(ss1.split())
        s2=ss2.split()
        res=[]
        # print(s1,type(s1),s2)
        for i in (s1):
            # print(i)
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in s2:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]==1:
                res.append(i)
                
        return res