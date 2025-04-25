// Problem: Minimum Size Subarray Sum
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/minimum-size-subarray-sum/
// Date: 2024-03-23

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if(target in nums):
            return 1
        if(sum(nums)<target):
            return 0
        minArray=len(nums)
        j=1
        i=0
        s=nums[i]
        while(True):
            if s>=target:
                minArray=min(minArray, abs(j-i))
                s-=nums[i]
                i+=1
                continue
            if(j>=len(nums)):
                break
            s+=nums[j]
            j+=1
        return minArray