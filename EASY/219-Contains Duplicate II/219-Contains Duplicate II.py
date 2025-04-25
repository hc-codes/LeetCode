// Problem: Contains Duplicate II
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/contains-duplicate-ii/
// Date: 2024-03-20

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k=min(k,len(nums)-1)
        present={}
        for i in range(k):
            if nums[i] in present:
                return True
            present[nums[i]]=True
        for i in range(k, len(nums)):
            if(nums[i] in present and present[nums[i]]):
                return True
            present[nums[i]]=True
            present[nums[i-k]]=False
        return False