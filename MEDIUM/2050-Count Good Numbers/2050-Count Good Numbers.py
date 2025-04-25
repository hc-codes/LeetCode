// Problem: Count Good Numbers
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/count-good-numbers/
// Date: 2024-11-09

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        odd = n//2
        even = n-odd # => n//2 + n%2
        print(odd,even)
        return (self.binaryExp(5, even)%mod *self.binaryExp(4, odd)%mod)%mod
    
    def binaryExp(self, x, n):
        mod = 1000000007
        if n==0:
            return 1

        if n%2==0:
            return self.binaryExp((x*x)%mod, n//2)
        else:
            return x*self.binaryExp((x*x)%mod, (n-1)//2)