// Problem: Final Value of Variable After Performing Operations
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
// Date: 2024-08-11

class Solution:
    def finalValueAfterOperations(self, op: List[str]) -> int:
        x=0
        for i in op:
            if i=="X++" or i=="++X":
                #print("hi")
                x+=1
            else:
                x-=1
        return x