// Problem: Maximum Average Subarray I
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/maximum-average-subarray-i/
// Date: 2024-10-14

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mxavg=0
        s=0
        for i in range(k):
            s+=nums[i]
        mxavg=s/k
        c=0
        i=k
        while(i<len(nums)):
            s+=nums[i]-nums[c]
            avg=s/k
            mxavg=max(mxavg,avg)
            i+=1
            c+=1
        return mxavg
            