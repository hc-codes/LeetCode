// Problem: Zigzag Conversion
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/zigzag-conversion/
// Date: 2024-09-29

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row = 0
        answer = [""] * numRows
        direction = 1
        for i in range(len(s)):
            # print(row,direction,answer)
            answer[row]+=s[i]
            row+=direction
            if row == -1 or row == numRows:
                direction *= -1
                row += (2*direction)
        return ''.join(answer)