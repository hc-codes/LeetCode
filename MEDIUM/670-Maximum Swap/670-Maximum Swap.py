// Problem: Maximum Swap
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/maximum-swap/
// Date: 2024-10-17

class Solution:
    def maximumSwap(self, nums: int) -> int:
        num=list(str(nums))
        mx="0"
        mx_i=-1
        # print(num[0])
        swap_i,swap_j=-1,-1
        # 5435
        for i in reversed(range(len(num))):
            if num[i]>mx:
                mx=num[i]
                mx_i=i
            if num[i]<mx:
                swap_i,swap_j=i,mx_i
        if swap_i!=-1:
            num[swap_i],num[swap_j]=num[swap_j],num[swap_i]
        return int(''.join(num))