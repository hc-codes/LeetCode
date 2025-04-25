// Problem: Search a 2D Matrix II
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/search-a-2d-matrix-ii/
// Date: 2024-08-03

class Solution:
    def searchMatrix(self, arr: List[List[int]], target: int) -> bool:
        if target>arr[len(arr)-1][len(arr[0])-1] or target<arr[0][0]:
            return False
        m=len(arr)
        n=len(arr[0])
        row=m-1
        col=0
        while(row>=0 and col<n):
            # print(arr[row][col])
            if arr[row][col]==target:
                return True
            elif arr[row][col]>target:
                row-=1
            else:
                col+=1
        return False