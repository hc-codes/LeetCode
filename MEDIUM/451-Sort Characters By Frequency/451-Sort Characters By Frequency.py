// Problem: Sort Characters By Frequency
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/sort-characters-by-frequency/
// Date: 2024-08-14

class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        res=[]
        dd=sorted(d.items(), key=lambda x:x[1],reverse=True)
        # print((dd[0]))
        for i in dd:
            res.append(i[0]*i[1])
        return ''.join(res)
    