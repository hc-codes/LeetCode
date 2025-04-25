// Problem: Reverse Pairs
// Difficulty: HARD
// LeetCode URL: https://leetcode.com/problems/reverse-pairs/
// Date: 2024-07-25

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(arr,l,mid,high):
            left=l
            right=mid+1
            t=[]
            while(left<=mid and right<=high):
                if(arr[left]<=arr[right]):
                    t.append(arr[left])
                    left+=1
                else:
                    t.append(arr[right])
                    right+=1
            while(left<=mid):
                t.append(arr[left])
                left+=1
            while(right<=high):
                t.append(arr[right])
                right+=1
            for j in range(l,high+1):
                arr[j]=t[j-l]
        def countPairs(arr,left,mid,high):
            right=mid+1
            c=0
            for i in range(left,mid+1):
                while ((right<=high) and (arr[i]>(2*arr[right]))):
                    right+=1
                c+=right-(mid+1)
            return c
        def mergeSort(arr,left,high):
            c=0
            if left>=high:
                return c
            mid=(left+high)//2
            c+=mergeSort(arr,left,mid)
            c+=mergeSort(arr,mid+1,high)
            c+=countPairs(arr,left,mid,high)
            merge(arr,left,mid,high)
            return c
        return mergeSort(nums,0,len(nums)-1)
        