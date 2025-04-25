// Problem: Find a Peak Element II
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/find-a-peak-element-ii/
// Date: 2024-09-27

class Solution:
    def findPeakGrid(self, arr: List[List[int]]) -> List[int]:
        def findMax(arr,m,col):
            big=-1
            idx=-1
            for i in range(m):
                if arr[i][col]>big:
                    big=arr[i][col]
                    idx=i
            return idx    
        
        m=len(arr)
        n=len(arr[0])
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            row_index_max_ele=findMax(arr,m,mid)
        
            left_ele=arr[row_index_max_ele][mid-1] if mid-1 >=0 else -1
            right_ele=arr[row_index_max_ele][mid+1] if mid+1 < n else -1
            max_ele=arr[row_index_max_ele][mid]
            
            if max_ele>left_ele and max_ele>right_ele:
                return [row_index_max_ele,mid]
            elif max_ele<left_ele:
                right=mid-1
            else:
                left=mid+1
        return [-1,-1]
                