# Happy Number

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/happy-number/](https://leetcode.com/problems/happy-number/)

---

# Happy Number

**Difficulty**: Easy

**Tags**: Hash Table, Math, Two Pointers

---

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:


	Starting with any positive integer, replace the number by the sum of the squares of its digits.
	Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
	Those numbers for which this process ends in 1 are happy.


Return true if n is a happy number, and false if not.

&nbsp;
Example 1:


Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


Example 2:


Input: n = 2
Output: false


&nbsp;
Constraints:


	1 &lt;= n &lt;= 231 - 1



