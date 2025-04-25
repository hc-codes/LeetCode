# Check If N and Its Double Exist

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/check-if-n-and-its-double-exist/](https://leetcode.com/problems/check-if-n-and-its-double-exist/)

---

# Check If N and Its Double Exist

**Difficulty**: Easy

**Tags**: Array, Hash Table, Two Pointers, Binary Search, Sorting

---

Given an array arr of integers, check if there exist two indices i and j such that :


	i != j
	0 &lt;= i, j &lt; arr.length
	arr[i] == 2 * arr[j]


&nbsp;
Example 1:


Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]


Example 2:


Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.


&nbsp;
Constraints:


	2 &lt;= arr.length &lt;= 500
	-103 &lt;= arr[i] &lt;= 103



