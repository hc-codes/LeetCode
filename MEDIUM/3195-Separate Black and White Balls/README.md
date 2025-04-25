# Separate Black and White Balls

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/separate-black-and-white-balls/](https://leetcode.com/problems/separate-black-and-white-balls/)

---

# Separate Black and White Balls

**Difficulty**: Medium

**Tags**: Two Pointers, String, Greedy

---

There are n balls on a table, each ball has a color black or white.

You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.

In each step, you can choose two adjacent balls and swap them.

Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.

&nbsp;
Example 1:


Input: s = &quot;101&quot;
Output: 1
Explanation: We can group all the black balls to the right in the following way:
- Swap s[0] and s[1], s = &quot;011&quot;.
Initially, 1s are not grouped together, requiring at least 1 step to group them to the right.

Example 2:


Input: s = &quot;100&quot;
Output: 2
Explanation: We can group all the black balls to the right in the following way:
- Swap s[0] and s[1], s = &quot;010&quot;.
- Swap s[1] and s[2], s = &quot;001&quot;.
It can be proven that the minimum number of steps needed is 2.


Example 3:


Input: s = &quot;0111&quot;
Output: 0
Explanation: All the black balls are already grouped to the right.


&nbsp;
Constraints:


	1 &lt;= n == s.length &lt;= 105
	s[i] is either &#39;0&#39; or &#39;1&#39;.



