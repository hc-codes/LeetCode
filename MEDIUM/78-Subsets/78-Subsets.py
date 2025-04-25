// Problem: Subsets
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/subsets/
// Date: 2024-11-30

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        def dfs(res, idx):
            ans.append(res)
            if idx == len(nums):
                return           
            
            for i in range(idx, len(nums)):
                dfs(res + [nums[i]], i + 1)
            
        dfs([], 0)
        return ans