// Problem: Count Good Triplets
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/count-good-triplets/
// Date: 2025-04-14

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        prefix_sum = [0] * 1001
        # Prefix_sum[x] -> count of nums <= x
        res = 0
        n = len(arr)

        for j in range(n - 1):
            for k in range(j + 1, n):
                # we have to find the intersection of j & k.
                # How many values before j where abs conditions are met.
                if(abs(arr[j] - arr[k]) <= b):

                    r = min(arr[j] + a, arr[k] + c)
                    l = max(arr[j] - a, arr[k] - c)
                    l = max(l, 0)
                    r = min(r, 1000)
                    if l<= r:
                        res += prefix_sum[r] - (0 if l == 0 else prefix_sum[l-1])
            for i in range(arr[j], 1001):
                prefix_sum[i] += 1
        return res                   