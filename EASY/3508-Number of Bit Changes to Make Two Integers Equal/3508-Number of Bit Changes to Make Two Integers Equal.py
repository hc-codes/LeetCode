// Problem: Number of Bit Changes to Make Two Integers Equal
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/
// Date: 2024-07-27

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        return -1 if n&k!=k else (n^k).bit_count()