// Problem: Count Array Pairs Divisible by K
// Difficulty: HARD
// LeetCode URL: https://leetcode.com/problems/count-array-pairs-divisible-by-k/
// Date: 2024-10-01

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter = {} # This will store the what is the min required to make i divisible by k
        ans = 0
        n = len(nums)
        
        for i in range(n):
            gcd = math.gcd(k,nums[i]) # to find the min number that must be multiplied with i to make it divisible by k.
            want = k // gcd           # If i==k -> we can make a pair with all the elements and still it will be divisible by k.
            # print(ans,counter, "want=",want,"gcd=",gcd, "i=",nums[i])
            for num in counter:
                if num % want == 0: 
                    ans += counter[num] 
            counter[gcd] = counter.get(gcd,0)+1
        return ans