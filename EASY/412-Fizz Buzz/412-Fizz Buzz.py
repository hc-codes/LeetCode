// Problem: Fizz Buzz
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/fizz-buzz/
// Date: 2023-04-01

def _find(i):

        if i%3==0 and i%5==0:

            return "FizzBuzz"

        if i%3==0:

            return "Fizz"

        if i%5==0:

            return "Buzz"

        return str(i)
class Solution(object):


    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        for i in range(1,n+1):
            res.append(_find(i))
        return res
    