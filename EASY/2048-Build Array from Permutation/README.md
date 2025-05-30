# Build Array from Permutation

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/build-array-from-permutation/](https://leetcode.com/problems/build-array-from-permutation/)

---

# Build Array from Permutation

**Difficulty**: Easy

**Tags**: Array, Simulation

---

Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 &lt;= i &lt; nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

&nbsp;
Example 1:


Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]

Example 2:


Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]

&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 1000
	0 &lt;= nums[i] &lt; nums.length
	The elements in nums are distinct.


&nbsp;
Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?


