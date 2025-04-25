// Problem: Jump Game
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/jump-game/
// Date: 2024-07-23

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            print(target)
            if nums[i]+i>=target:
                target=i
                continue
            
        return target == 0