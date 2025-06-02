# Last updated: 6/2/2025, 5:18:12 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def dfs(res,idx):
            ans.append(res)
            for i in range(idx,len(nums)):
                dfs(res+[nums[i]],i+1)
        
        
        dfs([],0)
        return ans