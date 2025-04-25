# Longest Arithmetic Subsequence

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/longest-arithmetic-subsequence/](https://leetcode.com/problems/longest-arithmetic-subsequence/)

---

# Longest Arithmetic Subsequence

**Difficulty**: Medium

**Tags**: Array, Hash Table, Binary Search, Dynamic Programming

---

Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:


	A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
	A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 &lt;= i &lt; seq.length - 1).


&nbsp;
Example 1:


Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.


Example 2:


Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].


Example 3:


Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].


&nbsp;
Constraints:


	2 &lt;= nums.length &lt;= 1000
	0 &lt;= nums[i] &lt;= 500



