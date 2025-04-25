// Problem: Koko Eating Bananas
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/koko-eating-bananas/
// Date: 2024-08-17

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findTotalTime(arr, banana_per_hour):
            time=0
            for i in range(len(arr)):
                time=time+ceil(arr[i]/banana_per_hour)
                # print("time=",time)
            return time
        l=1
        r=max(piles)
        ans=r
        while(l<=r):
            m=(l+r)//2
            time_taken=findTotalTime(piles,m)
            # print(time_taken)
            if time_taken>h:
                l=m+1
            else:
                r=m-1
                ans=min(ans,m)
        return ans