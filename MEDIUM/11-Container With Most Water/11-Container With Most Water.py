// Problem: Container With Most Water
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/container-with-most-water/
// Date: 2024-05-09

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if(len(height)<2):
            return min(height[0],height[1])*len(height)
        i=0
        j=len(height)-1
        max_area=0
        while(i<j):
            area=min(height[i],height[j])*(j-i)
            max_area=max(area,max_area)
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return max_area