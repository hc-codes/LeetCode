// Problem: Reverse String
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/reverse-string/
// Date: 2024-10-05

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        print(j)
        while(i<j):
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
            #print(s)