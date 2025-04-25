// Problem: Maximum Length of Repeated Subarray
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/maximum-length-of-repeated-subarray/
// Date: 2024-03-24

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if(nums1==nums2):
            return len(nums1)
        if(len(nums1)<=1 or len(nums2)<=1):
            return min(len(nums1),len(nums2))
        m,n=len(nums1),len(nums2)
        mL=0
        for i in range(-n+1, m):
            count=0
            for j in range(n):
                if(i+j<0):
                    continue
                if(i+j>=m):
                    break
                if(nums1[i+j]==nums2[j]):
                    count+=1
                    mL=max(mL,count)
                else:
                    count=0
        return mL