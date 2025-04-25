# Group Anagrams

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/)

---

# Group Anagrams

**Difficulty**: Medium

**Tags**: Array, Hash Table, String, Sorting

---

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

&nbsp;
Example 1:


Input: strs = [&quot;eat&quot;,&quot;tea&quot;,&quot;tan&quot;,&quot;ate&quot;,&quot;nat&quot;,&quot;bat&quot;]

Output: [[&quot;bat&quot;],[&quot;nat&quot;,&quot;tan&quot;],[&quot;ate&quot;,&quot;eat&quot;,&quot;tea&quot;]]

Explanation:


	There is no string in strs that can be rearranged to form &quot;bat&quot;.
	The strings &quot;nat&quot; and &quot;tan&quot; are anagrams as they can be rearranged to form each other.
	The strings &quot;ate&quot;, &quot;eat&quot;, and &quot;tea&quot; are anagrams as they can be rearranged to form each other.



Example 2:


Input: strs = [&quot;&quot;]

Output: [[&quot;&quot;]]


Example 3:


Input: strs = [&quot;a&quot;]

Output: [[&quot;a&quot;]]


&nbsp;
Constraints:


	1 &lt;= strs.length &lt;= 104
	0 &lt;= strs[i].length &lt;= 100
	strs[i] consists of lowercase English letters.



