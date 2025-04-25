// Problem: Maximum Sum of Distinct Subarrays With Length K
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
// Date: 2024-11-19

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        
        left = 0
        res = 0
        s = 0
        mf = 0
        
        for right in range(len(nums)):
            if nums[right] not in d:
                d[nums[right]] = 1
            else:
                d[nums[right]] += 1
                
            s += nums[right]
            
            # mf = max(mf, d[nums[right]])
            
            if right - left + 1 > k:
                if d[nums[left]] == 1:
                    d.pop(nums[left])
                else:
                    d[nums[left]] -= 1
                    
                s -= nums[left]
                left += 1
            
            if len(d) == right - left + 1 == k:
                res = max(res, s)                
            # print(s)
        return res