// Problem: Pascal's Triangle
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/pascals-triangle/
// Date: 2024-07-24

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res=[]
        for i in range(1,n+1):
            c=1
            a=[]
            for j in range(1,i+1):
                a.append(c)
                c=c*(i-j)//j
            res.append(a)
        return res