// Problem: Merge Sorted Array
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/merge-sorted-array/
// Date: 2024-07-24

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x=m+n-1
        m-=1
        n-=1
        while(n>=0):
            print(nums1)
            if m>=0 and nums1[m]>nums2[n]:
                nums1[x]=nums1[m]
                m-=1
            else:
                nums1[x]=nums2[n]
                n-=1
            x-=1