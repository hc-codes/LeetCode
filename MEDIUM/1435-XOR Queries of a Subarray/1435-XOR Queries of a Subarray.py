// Problem: XOR Queries of a Subarray
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/xor-queries-of-a-subarray/
// Date: 2024-09-14

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if not queries:
            return
        pre=[arr[0]]
        res=[]
        # print("pre=",pre[-1])
        for i in range(1,len(arr)):
            pre.append(pre[-1]^arr[i])
        # print(pre)
        for query in queries:
            if query[0]==0:
                res.append(pre[query[1]])
            else:
                res.append(pre[query[1]]^pre[query[0]-1])
        return res