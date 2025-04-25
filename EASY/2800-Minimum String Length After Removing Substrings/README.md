# Minimum String Length After Removing Substrings

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/minimum-string-length-after-removing-substrings/](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/)

---

# Minimum String Length After Removing Substrings

**Difficulty**: Easy

**Tags**: String, Stack, Simulation

---

You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings &quot;AB&quot; or &quot;CD&quot; from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new &quot;AB&quot; or &quot;CD&quot; substrings.

&nbsp;
Example 1:


Input: s = &quot;ABFCACDB&quot;
Output: 2
Explanation: We can do the following operations:
- Remove the substring &quot;ABFCACDB&quot;, so s = &quot;FCACDB&quot;.
- Remove the substring &quot;FCACDB&quot;, so s = &quot;FCAB&quot;.
- Remove the substring &quot;FCAB&quot;, so s = &quot;FC&quot;.
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.

Example 2:


Input: s = &quot;ACBBD&quot;
Output: 5
Explanation: We cannot do any operations on the string so the length remains the same.


&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 100
	s&nbsp;consists only of uppercase English letters.



