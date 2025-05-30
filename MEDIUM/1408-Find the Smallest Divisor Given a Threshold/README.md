# Find the Smallest Divisor Given a Threshold

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)

---

# Find the Smallest Divisor Given a Threshold

**Difficulty**: Medium

**Tags**: Array, Binary Search

---

Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division&#39;s result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so&nbsp;that there will be an answer.

&nbsp;
Example 1:


Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 


Example 2:


Input: nums = [44,22,33,11,1], threshold = 5
Output: 44


&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 5 * 104
	1 &lt;= nums[i] &lt;= 106
	nums.length &lt;= threshold &lt;= 106



