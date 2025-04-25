# Count Good Numbers

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/count-good-numbers/](https://leetcode.com/problems/count-good-numbers/)

---

# Count Good Numbers

**Difficulty**: Medium

**Tags**: Math, Recursion

---

A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).


	For example, &quot;2582&quot; is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, &quot;3245&quot; is not good because 3 is at an even index but is not even.


Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

&nbsp;
Example 1:


Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are &quot;0&quot;, &quot;2&quot;, &quot;4&quot;, &quot;6&quot;, &quot;8&quot;.


Example 2:


Input: n = 4
Output: 400


Example 3:


Input: n = 50
Output: 564908303


&nbsp;
Constraints:


	1 &lt;= n &lt;= 1015



