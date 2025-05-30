# Count Array Pairs Divisible by K

**Difficulty**: HARD

**URL**: [https://leetcode.com/problems/count-array-pairs-divisible-by-k/](https://leetcode.com/problems/count-array-pairs-divisible-by-k/)

---

# Count Array Pairs Divisible by K

**Difficulty**: Hard

**Tags**: Array, Math, Number Theory

---

Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:


	0 &lt;= i &lt; j &lt;= n - 1 and
	nums[i] * nums[j] is divisible by k.


&nbsp;
Example 1:


Input: nums = [1,2,3,4,5], k = 2
Output: 7
Explanation: 
The 7 pairs of indices whose corresponding products are divisible by 2 are
(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), and (3, 4).
Their products are 2, 4, 6, 8, 10, 12, and 20 respectively.
Other pairs such as (0, 2) and (2, 4) have products 3 and 15 respectively, which are not divisible by 2.    


Example 2:


Input: nums = [1,2,3,4], k = 5
Output: 0
Explanation: There does not exist any pair of indices whose corresponding product is divisible by 5.


&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 105
	1 &lt;= nums[i], k &lt;= 105



