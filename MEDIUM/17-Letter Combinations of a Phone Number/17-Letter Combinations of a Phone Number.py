// Problem: Letter Combinations of a Phone Number
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
// Date: 2024-11-08

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d={}
        d["2"]="abc"
        d["3"]="def"
        d["4"]="ghi"
        d["5"]="jkl"
        d["6"]="mno"
        d["7"]="pqrs"
        d["8"]="tuv"
        d["9"]="wxyz"
        
        ans=[]
    
        def dfs(res, nxt):
            # print(res, nxt)
            if not nxt:
                ans.append(res)
                return
            
            for i in d[nxt[0]]:         # Here we take the first digit only -> Gets the mapping from dict i.e "abc"
                dfs(res+i, nxt[1:])     # Here we take the rest of the digits -> create the combination of letter from each digits of first previous one -> ad, ae, af, bd, be, bf,cd,ce,cf
               
        dfs("",digits)
        return ans