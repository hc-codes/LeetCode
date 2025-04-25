// Problem: Wiggle Subsequence
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/wiggle-subsequence/
// Date: 2024-07-15

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # c=1
        # a=[]
        # for i in range(1,len(nums)):
        #     d=nums[i]-nums[i-1]
        #     ct=False
        #     # print(ct,d)
        #     if(c==1 and d!=0):
        #         c+=1
        #         a.append(d)
        #         continue
        #     if d==0:
        #         continue
        #     elif d>0 and a[-1]<0:
        #         ct=False
        #         c+=1
        #         a.append(d)
        #     elif d<0 and a[-1]>0:
        #         ct=True
        #         c+=1
        #         a.append(d)
            # print(ct,d)

            # if(not ct and d>0):
            #     c+=1
            #     ct=True
            #     a.append(d)
            # elif(ct and d<0):
            #     c+=1
            #     ct=False
            #     a.append(d)
            # else:
            #     continue
        # print(a)
        # return c
        a=[nums[i]-nums[i-1] for i in range(1,len(nums)) if nums[i]-nums[i-1]!=0]
        if(len(a)==0):
            return 1
        c=2
        # print(a)
        for i in range(1,len(a)):
            if ((a[i-1]>0 and a[i]<0) or (a[i-1]<0 and a[i]>0)):
                c+=1
        return c
