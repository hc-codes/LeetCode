// Problem: Count the Number of Fair Pairs
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/count-the-number-of-fair-pairs/
// Date: 2024-11-13

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def fun(nums, value):
            i=0
            j=len(nums)-1
            c=0
            while i<j:
                s=nums[i]+nums[j]
                if s<value:
                    c+=j-i
                    i+=1
                else:
                    j-=1
            return c
        r=fun(nums, upper+1)
        k=fun(nums,lower)
        # print(r,k)
        return r-k