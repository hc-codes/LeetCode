# Median of Two Sorted Arrays

**Difficulty**: HARD

**URL**: [https://leetcode.com/problems/median-of-two-sorted-arrays/](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---

# Median of Two Sorted Arrays

**Difficulty**: Hard

**Tags**: Array, Binary Search, Divide and Conquer

---

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

&nbsp;
Example 1:


Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:


Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


&nbsp;
Constraints:


	nums1.length == m
	nums2.length == n
	0 &lt;= m &lt;= 1000
	0 &lt;= n &lt;= 1000
	1 &lt;= m + n &lt;= 2000
	-106 &lt;= nums1[i], nums2[i] &lt;= 106



