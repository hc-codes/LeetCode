// Problem: Pascal's Triangle II
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/pascals-triangle-ii/
// Date: 2024-07-23

class Solution:
    def getRow(self, n: int) -> List[int]:
        for i in range(n+1,n+2):
            c=1
            a=[]
            for j in range(1,i+1):
                a.append(c)
                c=(c*(i-j)//j)
            return(a)