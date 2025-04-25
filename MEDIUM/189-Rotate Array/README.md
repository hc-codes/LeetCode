# Rotate Array

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/rotate-array/](https://leetcode.com/problems/rotate-array/)

---

# Rotate Array

**Difficulty**: Medium

**Tags**: Array, Math, Two Pointers

---

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

&nbsp;
Example 1:


Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Example 2:


Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 105
	-231 &lt;= nums[i] &lt;= 231 - 1
	0 &lt;= k &lt;= 105


&nbsp;
Follow up:


	Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
	Could you do it in-place with O(1) extra space?



