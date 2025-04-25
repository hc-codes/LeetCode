// Problem: Minimum Index Sum of Two Lists
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/minimum-index-sum-of-two-lists/
// Date: 2024-09-03

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if not list1 or not list2:
            return
        d={}
        for i in range(len(list1)):
            if list1[i] not in d:
                d[list1[i]]=i
            else:
                continue
        sm=len(list1)+len(list2)
        res=[]
        print(d)
        for i in range(len(list2)):
            if list2[i] in d:
                s=i+d[list2[i]]
                # print(list2[i])
                if s<sm:
                    sm=s
                    res=[]
                    res.append(list2[i])
                    continue
                if s==sm:
                    res.append(list2[i])
        return res
                