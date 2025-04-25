// Problem: Combination Sum
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/combination-sum/
// Date: 2024-11-10

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(res, i):
            if sum(res)>target:
                return
            if sum(res)==target:
                ans.append(res)
                return
            for j in range(i,len(nums)):
                dfs(res+[nums[j]], j)
            return ans
        
        return dfs([],0)