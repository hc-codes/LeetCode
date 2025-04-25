# Minimum Index Sum of Two Lists

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/minimum-index-sum-of-two-lists/](https://leetcode.com/problems/minimum-index-sum-of-two-lists/)

---

# Minimum Index Sum of Two Lists

**Difficulty**: Easy

**Tags**: Array, Hash Table, String

---

Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.

&nbsp;
Example 1:


Input: list1 = [&quot;Shogun&quot;,&quot;Tapioca Express&quot;,&quot;Burger King&quot;,&quot;KFC&quot;], list2 = [&quot;Piatti&quot;,&quot;The Grill at Torrey Pines&quot;,&quot;Hungry Hunter Steakhouse&quot;,&quot;Shogun&quot;]
Output: [&quot;Shogun&quot;]
Explanation: The only common string is &quot;Shogun&quot;.


Example 2:


Input: list1 = [&quot;Shogun&quot;,&quot;Tapioca Express&quot;,&quot;Burger King&quot;,&quot;KFC&quot;], list2 = [&quot;KFC&quot;,&quot;Shogun&quot;,&quot;Burger King&quot;]
Output: [&quot;Shogun&quot;]
Explanation: The common string with the least index sum is &quot;Shogun&quot; with index sum = (0 + 1) = 1.


Example 3:


Input: list1 = [&quot;happy&quot;,&quot;sad&quot;,&quot;good&quot;], list2 = [&quot;sad&quot;,&quot;happy&quot;,&quot;good&quot;]
Output: [&quot;sad&quot;,&quot;happy&quot;]
Explanation: There are three common strings:
&quot;happy&quot; with index sum = (0 + 1) = 1.
&quot;sad&quot; with index sum = (1 + 0) = 1.
&quot;good&quot; with index sum = (2 + 2) = 4.
The strings with the least index sum are &quot;sad&quot; and &quot;happy&quot;.


&nbsp;
Constraints:


	1 &lt;= list1.length, list2.length &lt;= 1000
	1 &lt;= list1[i].length, list2[i].length &lt;= 30
	list1[i] and list2[i] consist of spaces &#39; &#39; and English letters.
	All the strings of list1 are unique.
	All the strings of list2 are unique.
	There is at least a common string between list1 and list2.



