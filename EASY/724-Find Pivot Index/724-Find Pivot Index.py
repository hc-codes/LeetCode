// Problem: Find Pivot Index
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/find-pivot-index/
// Date: 2024-10-14

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        d={0:-1}
        s=sum(nums)
        ls=0
        rs=s
        for i in range(len(nums)):
            # print(ls,rs)
            rs=rs-nums[i]
            if ls==rs:
                return i
            ls=ls+nums[i]
        return -1