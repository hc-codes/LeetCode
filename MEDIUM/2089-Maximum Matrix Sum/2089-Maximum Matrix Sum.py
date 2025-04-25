// Problem: Maximum Matrix Sum
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/maximum-matrix-sum/
// Date: 2024-11-24

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_num = 99999999
        neg = 0
        s=0
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[i][j] < 0:
                    neg += 1
                min_num = min(min_num, abs(matrix[i][j]))
                s += abs(matrix[i][j])
        print(s, min_num, neg)
        return s - 2 * min_num if neg % 2 == 1 else s