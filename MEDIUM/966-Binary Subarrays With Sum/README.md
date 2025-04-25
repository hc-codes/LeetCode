# Binary Subarrays With Sum

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/binary-subarrays-with-sum/](https://leetcode.com/problems/binary-subarrays-with-sum/)

---

# Binary Subarrays With Sum

**Difficulty**: Medium

**Tags**: Array, Hash Table, Sliding Window, Prefix Sum

---

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

&nbsp;
Example 1:


Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]


Example 2:


Input: nums = [0,0,0,0,0], goal = 0
Output: 15


&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 3 * 104
	nums[i] is either 0 or 1.
	0 &lt;= goal &lt;= nums.length



