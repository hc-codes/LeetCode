// Problem: Number of Good Pairs
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/number-of-good-pairs/
// Date: 2024-09-01

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if not nums: return
        res=0
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                res+=dic[i]
                dic[i]+=1
        return res