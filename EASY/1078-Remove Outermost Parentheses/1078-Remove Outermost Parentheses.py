// Problem: Remove Outermost Parentheses
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/remove-outermost-parentheses/
// Date: 2024-08-10

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        c=1
        i=1
        while i<len(s):
            if s[i]=="(":
                c+=1
            else:
                c-=1
            if c==0:
                i+=1
                c=1
            else:
                stack.append(s[i])
            i+=1
        return "".join(stack)