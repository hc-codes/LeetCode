// Problem: Median of Two Sorted Arrays
// Difficulty: HARD
// LeetCode URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
// Date: 2024-08-06

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2=len(nums1),len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)
        n=n1+n2
        left=(n1+n2+1)//2
        l=0
        r=n1
        while(l<=r):
            m1=(l+r)//2
            m2=left-m1
            l1 = float('-inf') if m1 == 0 else nums1[m1 - 1]
            l2 = float('-inf') if m2 == 0 else nums2[m2 - 1]
            r1 = float('inf') if m1 == n1 else nums1[m1]
            r2 = float('inf') if m2 == n2 else nums2[m2]
            
            if l1<=r2 and l2<=r1:
                if n%2==1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1>r2:
                r=m1-1
            else:
                l=m1+1
        return 0.0