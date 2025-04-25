// Problem: Find the Index of the First Occurrence in a String
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
// Date: 2023-11-30

class Solution:
    def strStr(self, text: str, pattern: str) -> int:
        pattern_hash = self.hash_string(pattern)
        start=0
        end = len(pattern)
        while(end<=len(text)):
            sub = text[start:end]
            if(self.hash_string(sub)==pattern_hash):
                if(sub==pattern):
                    return start
            start+=1
            end+=1
        return -1
    def hash_string(self, s):
        prime = 101
        hash_value = 0
        for char in s:
            hash_value = (hash_value * 256 + ord(char)) % prime
        return hash_value