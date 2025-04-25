// Problem: Find the Smallest Divisor Given a Threshold
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
// Date: 2024-07-31

class Solution:
    def smallestDivisor(self, arr: List[int], threshold: int) -> int:
        def divideAndFindSum(arr,divisor):
            s=0
            for i in range(len(arr)):
                res=ceil(arr[i]/divisor)
                s=s+res
            return s
        l=1
        r=max(arr)
        ans=s=0
        while(l<=r):
            m=(l+r)//2
            s = divideAndFindSum(arr,m)
            if(s<=threshold):
                r=m-1
                ans=m
            else:
                l=m+1
        return ans