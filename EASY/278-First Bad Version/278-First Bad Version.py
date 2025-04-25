// Problem: First Bad Version
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/first-bad-version/
// Date: 2024-07-29

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ans=9999999999999
        l=0
        r=n
        while(l<=r):
            m=(l+r)//2
            res=isBadVersion(m)
            if res:
                r=m-1
                ans=min(ans,m)
            else:
                l=m+1
        return ans