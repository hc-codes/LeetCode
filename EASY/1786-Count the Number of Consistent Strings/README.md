# Count the Number of Consistent Strings

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/count-the-number-of-consistent-strings/](https://leetcode.com/problems/count-the-number-of-consistent-strings/)

---

# Count the Number of Consistent Strings

**Difficulty**: Easy

**Tags**: Array, Hash Table, String, Bit Manipulation, Counting

---

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

&nbsp;
Example 1:


Input: allowed = &quot;ab&quot;, words = [&quot;ad&quot;,&quot;bd&quot;,&quot;aaab&quot;,&quot;baa&quot;,&quot;badab&quot;]
Output: 2
Explanation: Strings &quot;aaab&quot; and &quot;baa&quot; are consistent since they only contain characters &#39;a&#39; and &#39;b&#39;.


Example 2:


Input: allowed = &quot;abc&quot;, words = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;ab&quot;,&quot;ac&quot;,&quot;bc&quot;,&quot;abc&quot;]
Output: 7
Explanation: All strings are consistent.


Example 3:


Input: allowed = &quot;cad&quot;, words = [&quot;cc&quot;,&quot;acd&quot;,&quot;b&quot;,&quot;ba&quot;,&quot;bac&quot;,&quot;bad&quot;,&quot;ac&quot;,&quot;d&quot;]
Output: 4
Explanation: Strings &quot;cc&quot;, &quot;acd&quot;, &quot;ac&quot;, and &quot;d&quot; are consistent.


&nbsp;
Constraints:


	1 &lt;= words.length &lt;= 104
	1 &lt;= allowed.length &lt;= 26
	1 &lt;= words[i].length &lt;= 10
	The characters in allowed are distinct.
	words[i] and allowed contain only lowercase English letters.



