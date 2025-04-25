# Kth Missing Positive Number

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/kth-missing-positive-number/](https://leetcode.com/problems/kth-missing-positive-number/)

---

# Kth Missing Positive Number

**Difficulty**: Easy

**Tags**: Array, Binary Search

---

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

&nbsp;
Example 1:


Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th&nbsp;missing positive integer is 9.


Example 2:


Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


&nbsp;
Constraints:


	1 &lt;= arr.length &lt;= 1000
	1 &lt;= arr[i] &lt;= 1000
	1 &lt;= k &lt;= 1000
	arr[i] &lt; arr[j] for 1 &lt;= i &lt; j &lt;= arr.length


&nbsp;
Follow up:

Could you solve this problem in less than O(n) complexity?


