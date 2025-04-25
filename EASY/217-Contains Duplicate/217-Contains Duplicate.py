// Problem: Contains Duplicate
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/contains-duplicate/
// Date: 2024-05-03

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited={}
        for i in nums:
            if i in visited:
                return True
            visited[i]=i
        return False