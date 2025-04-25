// Problem: Longest Consecutive Sequence
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/longest-consecutive-sequence/
// Date: 2024-09-25

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        ans=0
        for i in nums:
            length=1
            if i-1 not in nums:
                length=1
            else:
                continue
            while i+length in nums:
                length+=1
            ans=max(ans,length)
        return ans