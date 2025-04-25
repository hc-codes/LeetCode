# Replace Elements with Greatest Element on Right Side

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)

---

# Replace Elements with Greatest Element on Right Side

**Difficulty**: Easy

**Tags**: Array

---

Given an array arr,&nbsp;replace every element in that array with the greatest element among the elements to its&nbsp;right, and replace the last element with -1.

After doing so, return the array.

&nbsp;
Example 1:


Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --&gt; the greatest element to the right of index 0 is index 1 (18).
- index 1 --&gt; the greatest element to the right of index 1 is index 4 (6).
- index 2 --&gt; the greatest element to the right of index 2 is index 4 (6).
- index 3 --&gt; the greatest element to the right of index 3 is index 4 (6).
- index 4 --&gt; the greatest element to the right of index 4 is index 5 (1).
- index 5 --&gt; there are no elements to the right of index 5, so we put -1.


Example 2:


Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.


&nbsp;
Constraints:


	1 &lt;= arr.length &lt;= 104
	1 &lt;= arr[i] &lt;= 105



