// Problem: Find Minimum Operations to Make All Elements Divisible by Three
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
// Date: 2024-09-01

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            if i%3!=0:
                res+=1
        return res