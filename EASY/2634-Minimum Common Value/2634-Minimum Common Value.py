// Problem: Minimum Common Value
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/minimum-common-value/
// Date: 2024-10-26

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in nums2:
            l=0
            r=len(nums1)-1
            while(l<=r):
                m=(l+r)//2
                if nums1[m]==i:
                    return i
                elif nums1[m]<i:
                    l=m+1
                else:
                    r=m-1
        return -1