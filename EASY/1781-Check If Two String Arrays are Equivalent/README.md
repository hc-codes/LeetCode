# Check If Two String Arrays are Equivalent

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/)

---

# Check If Two String Arrays are Equivalent

**Difficulty**: Easy

**Tags**: Array, String

---

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

&nbsp;
Example 1:


Input: word1 = [&quot;ab&quot;, &quot;c&quot;], word2 = [&quot;a&quot;, &quot;bc&quot;]
Output: true
Explanation:
word1 represents string &quot;ab&quot; + &quot;c&quot; -&gt; &quot;abc&quot;
word2 represents string &quot;a&quot; + &quot;bc&quot; -&gt; &quot;abc&quot;
The strings are the same, so return true.

Example 2:


Input: word1 = [&quot;a&quot;, &quot;cb&quot;], word2 = [&quot;ab&quot;, &quot;c&quot;]
Output: false


Example 3:


Input: word1  = [&quot;abc&quot;, &quot;d&quot;, &quot;defg&quot;], word2 = [&quot;abcddefg&quot;]
Output: true


&nbsp;
Constraints:


	1 &lt;= word1.length, word2.length &lt;= 103
	1 &lt;= word1[i].length, word2[i].length &lt;= 103
	1 &lt;= sum(word1[i].length), sum(word2[i].length) &lt;= 103
	word1[i] and word2[i] consist of lowercase letters.



