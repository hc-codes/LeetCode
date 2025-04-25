// Problem: Minimum Add to Make Parentheses Valid
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
// Date: 2024-10-09

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=0
        ans=0
        for i in s:
            if i=="(":
                st+=1
            else:
                if st>0:
                    st-=1
                else:
                    ans+=1
        return st+ans
    
    #(()))
    