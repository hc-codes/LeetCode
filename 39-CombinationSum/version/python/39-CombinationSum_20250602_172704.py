# Last updated: 6/2/2025, 5:27:04 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(res, idx):
            if(sum(res) > target):
                return
            if(sum(res) == target):
                ans.append(res)
                return
            
            for i in range(idx, len(candidates)):
                dfs(res + [candidates[i]], i)
            return ans
        return dfs([], 0)
        