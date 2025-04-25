# Count Number of Nice Subarrays

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/count-number-of-nice-subarrays/](https://leetcode.com/problems/count-number-of-nice-subarrays/)

---

# Count Number of Nice Subarrays

**Difficulty**: Medium

**Tags**: Array, Hash Table, Math, Sliding Window, Prefix Sum

---

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

&nbsp;
Example 1:


Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].


Example 2:


Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.


Example 3:


Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 50000
	1 &lt;= nums[i] &lt;= 10^5
	1 &lt;= k &lt;= nums.length



