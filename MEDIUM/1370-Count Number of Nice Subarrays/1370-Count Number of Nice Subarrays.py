// Problem: Count Number of Nice Subarrays
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/count-number-of-nice-subarrays/
// Date: 2024-11-27

class Solution:
    def numberOfSubarrays(self, nums: List[int], goal: int) -> int:
        # same as binary array problem
        res = 0
        s = 0
        left = 0
        zeros = 0
        
        for right in range(len(nums)):
            s += nums[right] % 2
            
            while left < right and (s > goal or nums[left] % 2 == 0):
                if nums[left] % 2 == 1:
                    zeros = 0       # reset to 0 since we found a 1
                else:
                    zeros += 1
                s -= nums[left] % 2
                left += 1
            if s == goal:
                res += zeros + 1 # This will calcalate all the possible subarray with 0's
        return res