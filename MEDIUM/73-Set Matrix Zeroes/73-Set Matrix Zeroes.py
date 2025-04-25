// Problem: Set Matrix Zeroes
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/set-matrix-zeroes/
// Date: 2024-07-19

class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def nullifyRow(a,row):
            for i in range(len(a[0])):
                if a[row][i]!=0:
                    a[row][i]=0
        def nullifyCol(a,col):
            for i in range(len(a)):
                if a[i][col]!=0:
                    a[i][col]=0
                    
        rows=[False]*len(a)
        cols=[False]*len(a[0])
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j]==0:
                    rows[i]=True
                    cols[j]=True
        for i in range(len(rows)):
            if rows[i]:
                nullifyRow(a,i)
        for i in range(len(cols)):
            if cols[i]:
                nullifyCol(a,i)