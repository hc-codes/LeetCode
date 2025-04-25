// Problem: Defuse the Bomb
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/defuse-the-bomb/
// Date: 2024-11-18

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*len(code)
        
        if k==0: 
            return res
        
        left, s = 0, 0
        
        for right in range(n + abs(k)):
            s += code[right % n]

            # Window Exeeded i.e Shift
            if right - left + 1 > abs(k):
                s -= code[left]
                left = (left + 1) % n
                
            if right - left + 1 == abs(k):
                if k > 0:
                    res[(left - 1) % n] = s
                else:
                    res[(right + 1) % n] = s
        return res
                