// Problem: Monotonic Array
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/monotonic-array/
// Date: 2023-12-13

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prev=nums[0]
        inc=dec=False
        for i in nums:
            if(dec and inc):
                return False
            if(i==prev):
                continue
            if(i<prev):
                dec=True
            elif(i>prev):
                inc=True
            prev=i
        if(dec and inc):
                return False
        return True