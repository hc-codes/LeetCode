# Last updated: 5/31/2025, 12:50:22 PM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3]
        # [1,3,2]
        # [2,1,3]
        # [2,3,1]
        def rev(i,j):
            while(i<j):
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        breakpoint = -1
        for right in range(len(nums)-2,-1,-1):
            if nums[right] < nums[right + 1]:
                breakpoint = right
                break
        if breakpoint == -1:
            rev(0,len(nums)-1)
            return
        
        for right in range(len(nums)-1,-1,-1):
            if nums[right]>nums[breakpoint]:
                nums[right],nums[breakpoint] = nums[breakpoint],nums[right]
                break
        
        rev(breakpoint+1, len(nums)-1)
        
