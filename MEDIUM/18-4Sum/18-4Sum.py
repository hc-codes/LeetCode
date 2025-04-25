// Problem: 4Sum
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/4sum/
// Date: 2024-07-25

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=set()
        nums.sort()
        print(nums)
        for l in range(len(nums)):
            if l>0 and nums[l]==nums[l-1]:
                continue
            for i in range(l+1,len(nums)):
                if nums[i]==nums[i-1] and i-1 != l:
                    continue
                j=i+1
                k=len(nums)-1
                s=0
                while(j<k):
                    s=nums[l]+nums[i]+nums[j]+nums[k]
                    if s==target:
                        ans=(nums[l],nums[i],nums[j],nums[k])
                        res.add(ans)
                        j+=1
                        while nums[j]==nums[j-1] and j<k:
                            j+=1
                        while nums[k]==nums[k-1] and j<k:
                            k-=1
                    elif s>target:
                        k-=1
                    else:
                        j+=1
        return res