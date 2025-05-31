# Last updated: 5/31/2025, 1:49:41 PM
class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        d = {0:1}
        for i in range(len(a)):
            prefix_sum = prefix_sum + a[i]
            if prefix_sum - k in d:
                count += d[prefix_sum - k]
            if prefix_sum in d:
                d[prefix_sum] += 1
            else:
                d[prefix_sum] = 1
        return count
    
# Suppose prefixSum = 6 then find if 6-k is in d if yes add the count d[s-k] else update d[s] or add d[s]