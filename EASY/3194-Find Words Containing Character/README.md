# Find Words Containing Character

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/find-words-containing-character/](https://leetcode.com/problems/find-words-containing-character/)

---

# Find Words Containing Character

**Difficulty**: Easy

**Tags**: Array, String

---

You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

&nbsp;
Example 1:


Input: words = [&quot;leet&quot;,&quot;code&quot;], x = &quot;e&quot;
Output: [0,1]
Explanation: &quot;e&quot; occurs in both words: &quot;leet&quot;, and &quot;code&quot;. Hence, we return indices 0 and 1.


Example 2:


Input: words = [&quot;abc&quot;,&quot;bcd&quot;,&quot;aaaa&quot;,&quot;cbc&quot;], x = &quot;a&quot;
Output: [0,2]
Explanation: &quot;a&quot; occurs in &quot;abc&quot;, and &quot;aaaa&quot;. Hence, we return indices 0 and 2.


Example 3:


Input: words = [&quot;abc&quot;,&quot;bcd&quot;,&quot;aaaa&quot;,&quot;cbc&quot;], x = &quot;z&quot;
Output: []
Explanation: &quot;z&quot; does not occur in any of the words. Hence, we return an empty array.


&nbsp;
Constraints:


	1 &lt;= words.length &lt;= 50
	1 &lt;= words[i].length &lt;= 50
	x is a lowercase English letter.
	words[i] consists only of lowercase English letters.



