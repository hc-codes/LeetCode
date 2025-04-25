// Problem: Combination Sum III
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/combination-sum-iii/
// Date: 2024-11-07

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def dfs(res,idx):
            if sum(res)==n and len(res)==k:
                ans.append(res)
                return
            if len(res)==k:
                return
            for i in range(idx,10):
                dfs(res+[i],i+1)
        dfs([],1)
        return ans
                