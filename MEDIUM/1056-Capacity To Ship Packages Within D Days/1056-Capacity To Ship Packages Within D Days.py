// Problem: Capacity To Ship Packages Within D Days
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
// Date: 2024-07-31

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calculateDays(weights,minWeight):
            s=0
            d=1
            i=0
            for i in range(len(weights)):
                if(s+weights[i]>minWeight):
                    d+=1
                    s=weights[i]
                else:
                    s+=weights[i]
            return d
        l=max(weights)
        r=sum(weights)
        while(l<=r):
            m=(l+r)//2
            res=calculateDays(weights,m)
            if(res>days):
                l=m+1
            else:
                r=m-1
        return l