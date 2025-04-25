# Sort Characters By Frequency

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/sort-characters-by-frequency/](https://leetcode.com/problems/sort-characters-by-frequency/)

---

# Sort Characters By Frequency

**Difficulty**: Medium

**Tags**: Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting

---

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

&nbsp;
Example 1:


Input: s = &quot;tree&quot;
Output: &quot;eert&quot;
Explanation: &#39;e&#39; appears twice while &#39;r&#39; and &#39;t&#39; both appear once.
So &#39;e&#39; must appear before both &#39;r&#39; and &#39;t&#39;. Therefore &quot;eetr&quot; is also a valid answer.


Example 2:


Input: s = &quot;cccaaa&quot;
Output: &quot;aaaccc&quot;
Explanation: Both &#39;c&#39; and &#39;a&#39; appear three times, so both &quot;cccaaa&quot; and &quot;aaaccc&quot; are valid answers.
Note that &quot;cacaca&quot; is incorrect, as the same characters must be together.


Example 3:


Input: s = &quot;Aabb&quot;
Output: &quot;bbAa&quot;
Explanation: &quot;bbaA&quot; is also a valid answer, but &quot;Aabb&quot; is incorrect.
Note that &#39;A&#39; and &#39;a&#39; are treated as two different characters.


&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 5 * 105
	s consists of uppercase and lowercase English letters and digits.



