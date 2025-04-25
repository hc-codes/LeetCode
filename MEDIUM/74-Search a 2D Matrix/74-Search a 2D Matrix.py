// Problem: Search a 2D Matrix
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/search-a-2d-matrix/
// Date: 2024-08-03

class Solution:
    def searchMatrix(self, arr: List[List[int]], target: int) -> bool:
        if target>arr[len(arr)-1][len(arr[0])-1] or target<arr[0][0]:
            return False
        l=0
        m=len(arr)
        n=len(arr[0])
        r=(m*n)-1
        while(l<=r):
            mid=(l+r)//2
            row=mid//n
            col=mid%n
            if arr[row][col]==target:
                return True
            elif arr[row][col]<target:
                l=mid+1
            else:
                r=mid-1
        return False