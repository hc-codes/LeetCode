// Problem: Majority Element II
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/majority-element-ii/
// Date: 2024-07-20

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        res=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]>(len(nums)//3):
                res.append(i)
        return res