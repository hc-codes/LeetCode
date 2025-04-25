// Problem: Intersection of Two Arrays
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/intersection-of-two-arrays/
// Date: 2024-09-03

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return
        i=0
        j=0
        res=[]
        nums1.sort()
        nums2.sort()
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]==nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
                continue
            if nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return set(res)