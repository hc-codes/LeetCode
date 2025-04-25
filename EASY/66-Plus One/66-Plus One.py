// Problem: Plus One
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/plus-one/
// Date: 2023-07-27

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]=digits[-1]+1
            return digits
        nums = 0
        for i in digits:
            nums = nums* 10 + i
        nums = nums + 1
        return [int(x) for x in str(nums)]
