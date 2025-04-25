# Rotating the Box

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/rotating-the-box/](https://leetcode.com/problems/rotating-the-box/)

---

# Rotating the Box

**Difficulty**: Medium

**Tags**: Array, Two Pointers, Matrix

---

You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:


	A stone &#39;#&#39;
	A stationary obstacle &#39;*&#39;
	Empty &#39;.&#39;


The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles&#39; positions, and the inertia from the box&#39;s rotation does not affect the stones&#39; horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

&nbsp;
Example 1:




Input: boxGrid = [[&quot;#&quot;,&quot;.&quot;,&quot;#&quot;]]
Output: [[&quot;.&quot;],
&nbsp;        [&quot;#&quot;],
&nbsp;        [&quot;#&quot;]]


Example 2:




Input: boxGrid = [[&quot;#&quot;,&quot;.&quot;,&quot;*&quot;,&quot;.&quot;],
&nbsp;             [&quot;#&quot;,&quot;#&quot;,&quot;*&quot;,&quot;.&quot;]]
Output: [[&quot;#&quot;,&quot;.&quot;],
&nbsp;        [&quot;#&quot;,&quot;#&quot;],
&nbsp;        [&quot;*&quot;,&quot;*&quot;],
&nbsp;        [&quot;.&quot;,&quot;.&quot;]]


Example 3:




Input: boxGrid = [[&quot;#&quot;,&quot;#&quot;,&quot;*&quot;,&quot;.&quot;,&quot;*&quot;,&quot;.&quot;],
&nbsp;             [&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;*&quot;,&quot;.&quot;,&quot;.&quot;],
&nbsp;             [&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;.&quot;,&quot;#&quot;,&quot;.&quot;]]
Output: [[&quot;.&quot;,&quot;#&quot;,&quot;#&quot;],
&nbsp;        [&quot;.&quot;,&quot;#&quot;,&quot;#&quot;],
&nbsp;        [&quot;#&quot;,&quot;#&quot;,&quot;*&quot;],
&nbsp;        [&quot;#&quot;,&quot;*&quot;,&quot;.&quot;],
&nbsp;        [&quot;#&quot;,&quot;.&quot;,&quot;*&quot;],
&nbsp;        [&quot;#&quot;,&quot;.&quot;,&quot;.&quot;]]


&nbsp;
Constraints:


	m == boxGrid.length
	n == boxGrid[i].length
	1 &lt;= m, n &lt;= 500
	boxGrid[i][j] is either &#39;#&#39;, &#39;*&#39;, or &#39;.&#39;.



