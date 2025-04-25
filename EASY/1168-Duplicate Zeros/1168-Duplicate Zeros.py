// Problem: Duplicate Zeros
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/duplicate-zeros/
// Date: 2023-06-16

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        shift = arr.count(0)
        l = len(arr)
        for i in range(l-1, -1, -1):
            if(i+shift<l):
                arr[i+shift]=arr[i]
            if(arr[i]==0):
                shift-=1
                if(i+shift<l):
                    arr[i+shift]=arr[i]