// Problem: Generate Parentheses
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/generate-parentheses/
// Date: 2024-11-29

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def dfs(par, opens, closed, cc):
            if opens + closed == 2 * n:
                ans.append(par)
                
            if opens < n:
                dfs(par + "(", opens + 1, closed, cc + 1)
                
            if closed < opens:
                dfs(par + ")", opens, closed + 1, cc + 1)
                
        dfs("",0,0,1)
        return ans