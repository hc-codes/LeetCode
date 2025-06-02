# Last updated: 6/2/2025, 5:00:43 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(res, open, close):
            if  open + close == 2 * n:
                ans.append(res)
            
            if open < n:
                dfs(res + "(", open + 1, close)
            if close < open:
                dfs(res + ")", open, close + 1)
        
        dfs("", 0, 0)
        return ans