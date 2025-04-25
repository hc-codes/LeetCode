// Problem: Combinations
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/combinations/
// Date: 2024-11-06

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        
        def dfs(res, idx):
            if len(res)==k:
                ans.append(res)
                return
            
            for i in range(idx,n+1):
                dfs(res+[i],i+1)
        dfs([],1)
        return ans