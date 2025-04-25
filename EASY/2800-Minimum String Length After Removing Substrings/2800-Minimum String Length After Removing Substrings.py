// Problem: Minimum String Length After Removing Substrings
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
// Date: 2024-10-08

class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        for i in s:
            if not st:
                st.append(i)
                continue
            elif i=="B" and st[-1]=="A":
                st.pop()
            elif i=="D" and st[-1]=="C":
                st.pop()
            else:
                st.append(i)
        return len(st)
            