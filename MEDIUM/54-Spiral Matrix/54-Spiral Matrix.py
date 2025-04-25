// Problem: Spiral Matrix
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/spiral-matrix/
// Date: 2024-08-20

class Solution:
    def spiralOrder(self, a: List[List[int]]) -> List[int]:
        m=len(a)
        n=len(a[0])
        res=[]
        u=0
        l=0
        r=n-1
        b=m-1
        while(u<=b and l<=r):
            for j in range(u,r+1,1):
                res.append(a[u][j])
                # print(a[u][j])
            u+=1
            if not (u<=b and l<=r):
                break
            for k in range(u,b+1):
                print(k,r,b)
                res.append(a[k][r])
                # print(a[k][j])
            r-=1
            if not (u<=b and l<=r):
                break
            for s in range(r,l-1,-1):
                res.append(a[b][s])
                # print(a[b][s])
            b-=1
            if not (u<=b and l<=r):
                break
            for ll in range(b,u-1,-1):
                res.append(a[ll][l])
                print(a[ll][l])
            l+=1
        return res