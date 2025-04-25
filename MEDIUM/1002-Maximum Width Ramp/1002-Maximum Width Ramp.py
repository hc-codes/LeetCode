// Problem: Maximum Width Ramp
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/maximum-width-ramp/
// Date: 2024-10-10

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        if not nums: return 0
        stack=[]
        for i in range(len(nums)):
            if not stack or (nums[stack[-1]]>nums[i]):
                stack.append(i)
        mw=0
        for i in range(len(nums)-1,-1,-1):
            while(stack and nums[stack[-1]]<=nums[i]):
                mw=max(mw,i-stack.pop())
        return mw