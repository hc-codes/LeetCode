// Problem: Binary Subarrays With Sum
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/binary-subarrays-with-sum/
// Date: 2024-11-26

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         # Using Prefix sum
#         res = 0
#         csum = 0
#         prefix_sum = {}
#         for i in nums:
#             csum += i
#             if csum == goal:
#                 res += 1
            
#             # check if csum - goal in prefix_sum:
#             if csum - goal in prefix_sum:
#                 res += prefix_sum[csum-goal]
            
#             prefix_sum[csum] = prefix_sum.get(csum, 0) + 1
        
#         return res


# Using Venn diagram approach that is if we need to find some thing find total - find the others gives you the result 

#         def binarysum(nums, goal):
#             res = 0
#             s = 0
#             left = 0
#             for right in range(len(nums)):
#                 s += nums[right]
#                 while left <= right and s > goal:
#                     s -= nums[left]
#                     left += 1
#                 res += right - left + 1
#             return res  
#         return binarysum(nums, goal) - binarysum(nums, goal - 1)


# Count the number of zeros
        res = 0
        s = 0
        left = 0
        zeros = 0
        
        for right in range(len(nums)):
            s += nums[right]
            
            while left < right and (s > goal or nums[left] == 0):
                if nums[left] == 1:
                    zeros = 0       # reset to 0 since we found a 1
                else:
                    zeros += 1
                s -= nums[left]
                left += 1
            if s == goal:
                res += zeros + 1 # This will calcalate all the possible subarray with 0's
        return res