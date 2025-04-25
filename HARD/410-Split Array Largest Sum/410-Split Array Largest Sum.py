// Problem: Split Array Largest Sum
// Difficulty: HARD
// LeetCode URL: https://leetcode.com/problems/split-array-largest-sum/
// Date: 2024-08-05

class Solution:
    def splitArray(self, arr: List[int], k: int) -> int:
        if k>len(arr):
            return -1
        def findsum(arr,sum1):
            s,s1=0,1
            for i in range(len(arr)):
                if(s+arr[i]<=sum1):
                    s+=arr[i]
                else:
                    s1+=1
                    s=arr[i]
            return s1
        l=max(arr)
        r=sum(arr)
        while(l<=r):
            m=(l+r)//2
            res=findsum(arr,m)
            if res>k:
                l=m+1
            else:
                r=m-1
        return l