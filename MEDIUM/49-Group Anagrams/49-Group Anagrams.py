// Problem: Group Anagrams
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/group-anagrams/
// Date: 2023-08-12

class Solution:
    def groupAnagrams(self, strs):
        if(len(strs)==2):
            if self.isAnagram(strs[0],strs[1]):
                return[[strs[0],strs[1]]]
            else:
                return[[strs[0]],[strs[1]]]
        res=[]
        lst=[0]
        visited1=[]
        for i in range(len(strs)):
            if(strs[i] in visited1):
                continue
            lst=[]
            for j in range(i+1,len(strs)):
                if(self.isAnagram(strs[i],strs[j])):
                    lst.append(strs[j])
                    visited1.append(strs[j])
            if lst:
                visited1.append(strs[i])
                lst.append(strs[i])
                res.append(lst)
            else:
                res.append([strs[i]])
        return res
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)==0 and len(t)==0):
            return True
        if(len(s)!=len(t)):
            return False
        visited=[]
        for i in s:
            if i in visited:
                continue
            if ((s.count(i) != t.count(i)) or (i not in t)):
                return False
            visited.append(i)
        return True