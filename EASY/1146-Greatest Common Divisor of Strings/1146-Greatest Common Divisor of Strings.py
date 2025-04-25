// Problem: Greatest Common Divisor of Strings
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/greatest-common-divisor-of-strings/
// Date: 2024-01-13

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if( str2+str1 != str1+str2):
            return ""
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]