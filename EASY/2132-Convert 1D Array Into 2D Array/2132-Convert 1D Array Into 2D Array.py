// Problem: Convert 1D Array Into 2D Array
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/convert-1d-array-into-2d-array/
// Date: 2024-09-01

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = original[i * n + j]
        return res