// Problem: Trapping Rain Water
// Difficulty: HARD
// LeetCode URL: https://leetcode.com/problems/trapping-rain-water/
// Date: 2024-08-03

class Solution:
    def trap(self, h: List[int]) -> int:
        l=0
        ml,mr=0,0
        r=len(h)-1
        ans=0
        while(l<=r):
            ml=max(ml,h[l])
            mr=max(mr,h[r])
            if ml<mr:
                ans+=ml-h[l]
                l+=1
            else:
                ans+=mr-h[r]
                r-=1
        return ans
    