// Problem: Check If Array Pairs Are Divisible by k
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
// Date: 2024-10-04

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter=Counter()
        for i in arr:
            counter[i%k]+=1
        print(counter)
        for i in arr:
            if i%k==0:
                if counter[i%k]%2==1:
                    return False
            elif counter[i%k]!=counter[k-(i%k)]:
                return False
        return True

    # Create a tracker Counter that counts the remainders
    # If reminder=0 then it should have count 2 or multiples of 2 since 5 can only pair with multiples of 5 if k=5
    # For 1,9 to be a pair we should make sure that the count of 1%5==9%5 so that they can make pairs
    # This approach is similar to pre-sum