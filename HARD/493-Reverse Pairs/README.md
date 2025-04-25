# Reverse Pairs

**Difficulty**: HARD

**URL**: [https://leetcode.com/problems/reverse-pairs/](https://leetcode.com/problems/reverse-pairs/)

---

# Reverse Pairs

**Difficulty**: Hard

**Tags**: Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set

---

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:


	0 &lt;= i &lt; j &lt; nums.length and
	nums[i] &gt; 2 * nums[j].


&nbsp;
Example 1:


Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --&gt; nums[1] = 3, nums[4] = 1, 3 &gt; 2 * 1
(3, 4) --&gt; nums[3] = 3, nums[4] = 1, 3 &gt; 2 * 1


Example 2:


Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --&gt; nums[1] = 4, nums[4] = 1, 4 &gt; 2 * 1
(2, 4) --&gt; nums[2] = 3, nums[4] = 1, 3 &gt; 2 * 1
(3, 4) --&gt; nums[3] = 5, nums[4] = 1, 5 &gt; 2 * 1


&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 5 * 104
	-231 &lt;= nums[i] &lt;= 231 - 1



