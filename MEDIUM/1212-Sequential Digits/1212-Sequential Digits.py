// Problem: Sequential Digits
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/sequential-digits/
// Date: 2024-08-14

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q=deque(range(1,10))
        res=[]
        while q:
            n=q.popleft()
            if n>high:
                break
                continue
            if low<=n<=high:
                res.append(n)
            last=n%10
            if last<9:
                q.append(n*10+(last+1))
        print(q)
        return res
        