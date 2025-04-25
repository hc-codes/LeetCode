// Problem: Defanging an IP Address
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/defanging-an-ip-address/
// Date: 2024-08-11

class Solution:
    def defangIPaddr(self, a: str) -> str:
        res=""
        for i in a:
            if i==".":
                res+="["+i+"]"
            else:
                res+=i
        return res