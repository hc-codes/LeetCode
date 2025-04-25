// Problem: Divisible and Non-divisible Sums Difference
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
// Date: 2024-09-22

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s=0
        d=0
        for i in range(1,n+1):
            if i%m==0:
                d+=i
            else:
                s+=i
        return s-d