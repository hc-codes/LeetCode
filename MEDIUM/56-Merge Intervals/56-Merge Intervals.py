// Problem: Merge Intervals
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/merge-intervals/
// Date: 2024-07-24

class Solution:
    def merge(self, n: List[List[int]]) -> List[List[int]]:
        n.sort()
        res=[]
        for i in range(len(n)):
            if not res:
                res.append(n[i])
            else:
                x=res[-1]
                d=x[1]-x[0]+1
                cx=n[i]
                if x[1]>=cx[0]:
                    res[-1]=[min(x[0],cx[0]),max(cx[1],x[1])]
                else:
                    res.append(n[i])
        return res