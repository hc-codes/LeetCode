// Problem: Number of Visible People in a Queue
// Difficulty: HARD
// LeetCode URL: https://leetcode.com/problems/number-of-visible-people-in-a-queue/
// Date: 2024-05-12

class Solution:
    def canSeePersonsCount(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            vis=0
            while stack and stack[-1]<nums[i]:
                vis+=1
                res[i]=vis
                stack.pop()
            if stack:
                res[i]=vis+1
            stack.append(nums[i])
        return res
                