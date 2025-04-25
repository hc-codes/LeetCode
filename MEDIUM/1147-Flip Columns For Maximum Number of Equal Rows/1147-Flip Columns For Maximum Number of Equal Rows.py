// Problem: Flip Columns For Maximum Number of Equal Rows
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
// Date: 2024-11-22

class Solution:
    def maxEqualRowsAfterFlips(self, arr: List[List[int]]) -> int:
        d = defaultdict(int)
        
        for i in range(len(arr)):
            key, inverted_key = "", ""
            
            for j in range(len(arr[0])):
                key += str(arr[i][j])
                inverted_key += "0" if arr[i][j] == 1 else "1"
            
            if inverted_key in d:
                d[inverted_key] += 1
            else:
                d[key] += 1
        
        return max(d.values())                