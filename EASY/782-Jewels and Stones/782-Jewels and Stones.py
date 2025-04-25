// Problem: Jewels and Stones
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/jewels-and-stones/
// Date: 2024-08-11

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s=0
        for i in jewels:
            s+=stones.count(i)
        return s