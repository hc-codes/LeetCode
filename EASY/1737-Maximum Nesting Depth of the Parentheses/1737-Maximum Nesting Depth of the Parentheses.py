// Problem: Maximum Nesting Depth of the Parentheses
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
// Date: 2024-08-14

class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        big=0
        for i in s:
            if i=="(":
                c+=1
                big=max(big,c)
            elif i==")":
                c-=1
        return big