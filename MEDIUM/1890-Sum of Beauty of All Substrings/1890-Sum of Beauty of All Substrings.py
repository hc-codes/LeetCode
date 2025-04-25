// Problem: Sum of Beauty of All Substrings
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
// Date: 2024-08-15

class Solution:
    def beautySum(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            counter=Counter()
            for j in range(i,len(s)):
                counter[s[j]]+=1
                res=res+max(counter.values())-min(counter.values())
        return res
    
# here the main idea is to get all the substring and caluclate its beauty