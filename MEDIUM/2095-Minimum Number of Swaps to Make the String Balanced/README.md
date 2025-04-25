# Minimum Number of Swaps to Make the String Balanced

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/)

---

# Minimum Number of Swaps to Make the String Balanced

**Difficulty**: Medium

**Tags**: Two Pointers, String, Stack, Greedy

---

You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets &#39;[&#39; and n / 2 closing brackets &#39;]&#39;.

A string is called balanced if and only if:


	It is the empty string, or
	It can be written as AB, where both A and B are balanced strings, or
	It can be written as [C], where C is a balanced string.


You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

&nbsp;
Example 1:


Input: s = &quot;][][&quot;
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is &quot;[[]]&quot;.


Example 2:


Input: s = &quot;]]][[[&quot;
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = &quot;[]][][&quot;.
- Swap index 1 with index 5. s = &quot;[[][]]&quot;.
The resulting string is &quot;[[][]]&quot;.


Example 3:


Input: s = &quot;[]&quot;
Output: 0
Explanation: The string is already balanced.


&nbsp;
Constraints:


	n == s.length
	2 &lt;= n &lt;= 106
	n is even.
	s[i] is either &#39;[&#39; or &#39;]&#39;.
	The number of opening brackets &#39;[&#39; equals n / 2, and the number of closing brackets &#39;]&#39; equals n / 2.



