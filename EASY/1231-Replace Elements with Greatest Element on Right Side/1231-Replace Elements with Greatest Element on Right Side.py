// Problem: Replace Elements with Greatest Element on Right Side
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
// Date: 2024-07-20

class Solution:
    def replaceElements(self, a: List[int]) -> List[int]:
        leader=a[-1]
        for i in range(len(a)-2,-1,-1):
            if a[i]>leader:
                a[i],leader=leader,a[i]
                continue
            a[i]=leader
            
        a[-1]=-1
        return a