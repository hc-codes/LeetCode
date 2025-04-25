// Problem: Separate Black and White Balls
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/separate-black-and-white-balls/
// Date: 2024-10-15

class Solution:
    def minimumSteps(self, s: str) -> int:
        ones=0
        jumps=0
        for i in s:
            if i=="1":
                ones+=1
            else:
                jumps+=ones
        return jumps