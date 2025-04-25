# Check if Array Is Sorted and Rotated

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)

---

# Check if Array Is Sorted and Rotated

**Difficulty**: Easy

**Tags**: Array

---

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

&nbsp;
Example 1:


Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].


Example 2:


Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.


Example 3:


Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.




&nbsp;



&nbsp;


&nbsp;

&nbsp;






&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 100
	1 &lt;= nums[i] &lt;= 100



