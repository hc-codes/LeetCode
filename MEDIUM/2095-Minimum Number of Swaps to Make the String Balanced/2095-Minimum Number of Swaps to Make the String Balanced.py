// Problem: Minimum Number of Swaps to Make the String Balanced
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
// Date: 2024-10-09

class Solution:
    def minSwaps(self, s: str) -> int:
        ans=0
        for i in s:
            if i=="[":
                ans+=1
            else:
                if ans>0:
                    ans-=1
        return (ans+1)//2