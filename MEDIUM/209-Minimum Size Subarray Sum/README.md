# Minimum Size Subarray Sum

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/minimum-size-subarray-sum/](https://leetcode.com/problems/minimum-size-subarray-sum/)

---

# Minimum Size Subarray Sum

**Difficulty**: Medium

**Tags**: Array, Binary Search, Sliding Window, Prefix Sum

---

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

&nbsp;
Example 1:


Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.


Example 2:


Input: target = 4, nums = [1,4,4]
Output: 1


Example 3:


Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


&nbsp;
Constraints:


	1 &lt;= target &lt;= 109
	1 &lt;= nums.length &lt;= 105
	1 &lt;= nums[i] &lt;= 104


&nbsp;
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

