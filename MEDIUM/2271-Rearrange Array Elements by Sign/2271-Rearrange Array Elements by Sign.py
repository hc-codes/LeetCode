// Problem: Rearrange Array Elements by Sign
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/rearrange-array-elements-by-sign/
// Date: 2024-09-25

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        pos=0
        neg=1
        i=0
        while(i<len(nums)):
            if nums[i]>=0:
                ans[pos]=nums[i]
                pos+=2
            else:
                ans[neg]=nums[i]
                neg+=2
            i+=1
        return ans