// Problem: Permutations
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/permutations/
// Date: 2024-11-06

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        def dfs(n, res, idx):
            # print(n,idx, res)
            if not n:
                ans.append(res)
                return
            
            for i in range(len(n)):
                dfs(n[:i] + n[i+1:], res+[n[i]], i+1)
                
        dfs(nums,[],0)
        return ans