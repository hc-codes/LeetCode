// Problem: Happy Number
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/happy-number/
// Date: 2024-11-21

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = 0
        
        while True: 
            for i in str(n):
                num += int(i) ** 2
            if num == 1: return True
            if num in seen: return False

            seen.add(num)
            n = num
            num = 0
                
        return False