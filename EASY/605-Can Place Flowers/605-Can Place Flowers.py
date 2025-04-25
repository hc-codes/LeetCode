// Problem: Can Place Flowers
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/can-place-flowers/
// Date: 2024-02-03

class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        count=0
        for i in range(len(f)):
            if(f[i]==0):
                left= (i==0) or f[i-1]==0
                right= (i==len(f)-1) or f[i+1]==0
                if left and right:
                    f[i]=1
                    count+=1
        return count>=n
            