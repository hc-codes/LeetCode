// Problem: Subsets II
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/subsets-ii/
// Date: 2024-11-05

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def dfs(res, i):
            if i==len(nums):
                ans.append(res[:])
                return
                
            # if i >=len(nums): return

#           include
            res.append(nums[i])
            dfs(res, i+1)
            
            while i+1 <len(nums) and nums[i]==nums[i+1]: i=i+1
#           exclude
            res.pop()
            dfs(res, i+1)
            
            return ans
        
        return dfs([],0)