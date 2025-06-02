# Last updated: 6/2/2025, 4:51:52 PM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # This method is DFS using stack
        # Here we are using a stack to save the index and the substrings that are visited
        # so for each palin ss we are adding that to stack so once idx == len(s)
        # We can stack to check for another set of partioning with from the data in stack
        ans = []

        def isPal(s):
            return s == s[::-1]
        def dfs(res, idx):
            if idx >= len(s):
                ans.append(res)
            
            for i in range(idx, len(s)):
                ss = s[idx: i+1]
                if isPal(ss):
                    dfs(res + [ss], i + 1)
        
        dfs([], 0)
        return ans
        