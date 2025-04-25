# Merge Intervals

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/merge-intervals/](https://leetcode.com/problems/merge-intervals/)

---

# Merge Intervals

**Difficulty**: Medium

**Tags**: Array, Sorting

---

Given an array&nbsp;of intervals&nbsp;where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

&nbsp;
Example 1:


Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


Example 2:


Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


&nbsp;
Constraints:


	1 &lt;= intervals.length &lt;= 104
	intervals[i].length == 2
	0 &lt;= starti &lt;= endi &lt;= 104



