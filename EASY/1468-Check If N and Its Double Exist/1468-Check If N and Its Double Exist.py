// Problem: Check If N and Its Double Exist
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/check-if-n-and-its-double-exist/
// Date: 2024-12-07

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = Counter(arr)
        
        for i in arr:
            if i != 0 and i * 2 in d:
                return True
            if i==0 and d[i] > 1: return True
        return False