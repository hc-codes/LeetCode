# Shuffle String

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/shuffle-string/](https://leetcode.com/problems/shuffle-string/)

---

# Shuffle String

**Difficulty**: Easy

**Tags**: Array, String

---

You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

&nbsp;
Example 1:


Input: s = &quot;codeleet&quot;, indices = [4,5,6,7,0,2,1,3]
Output: &quot;leetcode&quot;
Explanation: As shown, &quot;codeleet&quot; becomes &quot;leetcode&quot; after shuffling.


Example 2:


Input: s = &quot;abc&quot;, indices = [0,1,2]
Output: &quot;abc&quot;
Explanation: After shuffling, each character remains in its position.


&nbsp;
Constraints:


	s.length == indices.length == n
	1 &lt;= n &lt;= 100
	s consists of only lowercase English letters.
	0 &lt;= indices[i] &lt; n
	All values of indices are unique.



