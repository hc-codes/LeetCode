// Problem: Subarray Sum Equals K
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/subarray-sum-equals-k/
// Date: 2024-09-25

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum=0
        d={}
        d[0]=1
        count_sub_arrays_with_sum_k=0
        for i in nums:
            prefixSum+=i
            if prefixSum-k in d:
                count_sub_arrays_with_sum_k+=d[prefixSum-k]
            if prefixSum in d:
                d[prefixSum]+=1
            else:
                d[prefixSum]=1
        return count_sub_arrays_with_sum_k
                
            