// Problem: Kth Missing Positive Number
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/kth-missing-positive-number/
// Date: 2024-08-01

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l=0
        r=len(arr)-1
        while(l<=r):
            m=(l+r)//2
            # print("arr[m]",arr[m],"m+1",m+1,"l=",l,"r=",r)
            if arr[m]-(m+1)>=k:
                r=m-1
            else:
                l=m+1
        return r+k+1