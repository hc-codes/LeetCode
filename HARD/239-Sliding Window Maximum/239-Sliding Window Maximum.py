// Problem: Sliding Window Maximum
// Difficulty: HARD
// LeetCode URL: https://leetcode.com/problems/sliding-window-maximum/
// Date: 2024-05-12

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if(k==1):
        #     return max(nums)
        # bigs=[0]*(len(nums)-k+1)
        # for i in range(len(nums)-k+1):
        #     big=nums[i]
        #     c=i+1
        #     while c<k:
        #         big=max(nums[c],big)
        #         c+=1
        #     bigs[i]=big
        #     k+=1
        # return bigs
        q=deque()
        res=[]
        for i in range(len(nums)):
            while q and q[0]<i-k+1:
                q.popleft()
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
            if(i>=k-1):
                res.append(nums[q[0]])
        return res