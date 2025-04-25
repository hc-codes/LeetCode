// Problem: Shortest Subarray to be Removed to Make Array Sorted
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
// Date: 2024-11-16

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Initilialize right as size of arr
        right=len(arr)-1
        
        # Iterate from right until its not sorted or start of arr.
        while right>0 and arr[right]>=arr[right-1]:
            right-=1
        
        # set ans=right since its the max we can remove if arr is in decreasing order
        ans=right
        left=0
        

        while(left<right and (left==0 or arr[left-1]<=arr[left])):
              
              # match the left most element on the right-side to be sorted with the right-most sorted element on the left. 
            while(right<len(arr) and arr[left]>arr[right]):
                right+=1
            ans=min(ans, right-left-1)
            left+=1
        return ans