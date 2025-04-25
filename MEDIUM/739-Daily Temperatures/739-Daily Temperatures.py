// Problem: Daily Temperatures
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/daily-temperatures/
// Date: 2024-05-01

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temp)
        for i in range(len(temp)):
            while stack and temp[stack[-1]]<temp[i]:
                r=stack.pop()
                ans[r]=i-r
            stack.append(i)
        return ans
        