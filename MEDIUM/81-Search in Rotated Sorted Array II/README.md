# Search in Rotated Sorted Array II

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/search-in-rotated-sorted-array-ii/](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

---

# Search in Rotated Sorted Array II

**Difficulty**: Medium

**Tags**: Array, Binary Search

---

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 &lt;= k &lt; nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

&nbsp;
Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 5000
	-104 &lt;= nums[i] &lt;= 104
	nums is guaranteed to be rotated at some pivot.
	-104 &lt;= target &lt;= 104


&nbsp;
Follow up: This problem is similar to&nbsp;Search in Rotated Sorted Array, but&nbsp;nums may contain duplicates. Would this affect the runtime complexity? How and why?


