// Problem: Kids With the Greatest Number of Candies
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
// Date: 2024-02-03

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        big = 0
        result=[]
        for i in candies:
            if i>big:
                big = i
        for i in candies:
            if i+extraCandies >= big:
                result.append(True)
            else:
                result.append(False)
        return result