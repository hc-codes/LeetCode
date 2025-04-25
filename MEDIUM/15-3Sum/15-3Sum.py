// Problem: 3Sum
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/3sum/
// Date: 2024-07-25

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            s=0
            while(j<k):
                s=nums[i]+nums[j]+nums[k]
                if s==0:
                    ans=(nums[i],nums[j],nums[k])
                    res.add(ans)
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                    while nums[k]==nums[k-1] and j<k:
                        k-=1
                elif s>0:
                    k-=1
                else:
                    j+=1
        return res
# Fix i, then use 2 pointer for rest of the list