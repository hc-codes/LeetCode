// Problem: Combination Sum II
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/combination-sum-ii/
// Date: 2024-11-11

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=set()
        def dfs(cur,cur_sum,i):
            if cur_sum==target:
                ans.add(tuple(cur))
                return
            if i>=len(nums): return
            if nums[i]+cur_sum <=target:
                if not cur or cur[-1] != nums[i]: 
                    dfs(cur,cur_sum,i+1)
                cur.append(nums[i])
                dfs(cur,cur_sum+nums[i],i+1)
                cur.pop()
        dfs([],0,0)
        return list(ans)