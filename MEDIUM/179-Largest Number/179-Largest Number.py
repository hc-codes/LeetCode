// Problem: Largest Number
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/largest-number/
// Date: 2024-09-20

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x,y):
            return (x+y)>(y+x)
            
        num = [str(x) for x in nums]
        num.sort(key=cmp_to_key(lambda x, y: (1 if (x+y)<(y+x) else -1)))
        return ''.join(num).lstrip('0') or '0'
    