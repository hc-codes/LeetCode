// Problem: N-th Tribonacci Number
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/n-th-tribonacci-number/
// Date: 2023-05-31

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=s=0
        b=1
        c=1
        if(n<=1):
            return n
        if(n<=2):
            return 1
        for i in range(n-2):
            s=a+b+c
            a=b
            b=c
            c=s
        return s