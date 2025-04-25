// Problem: Minimized Maximum of Products Distributed to Any Store
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
// Date: 2024-11-14

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        res=0
        
        def can_distribute(x):
            if x==0:
                return False
            stores=0
            for i in quantities:
                stores+=ceil(i/x)
            return stores<=n
        
        l=0
        r=max(quantities)
        while(l<=r):
            m=(l+r)//2
            if(can_distribute(m)):
                res=m
                r=m-1
            else:
                l=m+1
        return res