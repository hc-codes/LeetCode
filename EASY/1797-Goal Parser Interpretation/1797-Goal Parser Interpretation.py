// Problem: Goal Parser Interpretation
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/goal-parser-interpretation/
// Date: 2024-08-16

class Solution:
    def interpret(self, command: str) -> str:
        st=[]
        res=""
        for i in command:
            if i =="(":
                st.append(i)
            elif st and i==")":
                st.pop()
                res+="o"
            elif not st and i==")":
                st=[]
            else:
                st=[]
                res+=i
        return res