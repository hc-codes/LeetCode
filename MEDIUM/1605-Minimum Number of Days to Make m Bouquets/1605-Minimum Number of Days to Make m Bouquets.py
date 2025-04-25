// Problem: Minimum Number of Days to Make m Bouquets
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
// Date: 2024-07-29

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # print("m(k)",m*k)
        if (m*k)>len(bloomDay):
            return -1
        def findTotalFlowersBloomed(bloomDay, currentDay,k):
            totalFlowers=0
            bq=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=currentDay:
                    totalFlowers+=1
                    if totalFlowers==k:
                        bq+=1
                        totalFlowers=0
                else:
                    totalFlowers=0
            return bq
        sm=999999999999
        big=0
        for i in range(len(bloomDay)):
            big=max(big,bloomDay[i])
            sm=min(sm,bloomDay[i])
        l=sm
        r=big
        ans=big
        # print(sm,big)
        while(l<=r):
            mm=(l+r)//2
            totalFlowers=findTotalFlowersBloomed(bloomDay, mm,k)
            # print("mm=",mm,"tyotal=",totalFlowers)
            # print(totalFlowers, totalFlowers>=(m*k), m*k)
            if(totalFlowers>=m):
                ans=min(ans,mm)
                # print("ans=",ans)
                r=mm-1
            else:
                l=mm+1
        return ans