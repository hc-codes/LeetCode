# Sort the People

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/sort-the-people/](https://leetcode.com/problems/sort-the-people/)

---

# Sort the People

**Difficulty**: Easy

**Tags**: Array, Hash Table, String, Sorting

---

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people&#39;s heights.

&nbsp;
Example 1:


Input: names = [&quot;Mary&quot;,&quot;John&quot;,&quot;Emma&quot;], heights = [180,165,170]
Output: [&quot;Mary&quot;,&quot;Emma&quot;,&quot;John&quot;]
Explanation: Mary is the tallest, followed by Emma and John.


Example 2:


Input: names = [&quot;Alice&quot;,&quot;Bob&quot;,&quot;Bob&quot;], heights = [155,185,150]
Output: [&quot;Bob&quot;,&quot;Alice&quot;,&quot;Bob&quot;]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.


&nbsp;
Constraints:


	n == names.length == heights.length
	1 &lt;= n &lt;= 103
	1 &lt;= names[i].length &lt;= 20
	1 &lt;= heights[i] &lt;= 105
	names[i] consists of lower and upper case English letters.
	All the values of heights are distinct.



