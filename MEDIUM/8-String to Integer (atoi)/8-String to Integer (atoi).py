// Problem: String to Integer (atoi)
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/string-to-integer-atoi/
// Date: 2024-09-15

class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        # print(s)
        if len(s)==0:
            return 0
        n="1234567890"
        res=""
        neg=False
        if s[0]=="-":
            s=s[1:len(s)]
            neg=True
        elif s[0]=="+":
            s=s[1:len(s)]
        if len(s)==0:
            return 0
        for i in s:
            if i in n:
                if not (i=="0" and len(res)==0):
                    res+=i
            else:
                if len(res)==0:
                    return 0
                break
        if len(res)==0:
            return 0
        if neg:
            res="-"+res
        res=int(res)
        if res<-2**31:
            return -2**31
        if res>((2**31)-1):
            return (2**31)-1
        return res