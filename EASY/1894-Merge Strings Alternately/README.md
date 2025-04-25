# Merge Strings Alternately

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/merge-strings-alternately/](https://leetcode.com/problems/merge-strings-alternately/)

---

# Merge Strings Alternately

**Difficulty**: Easy

**Tags**: Two Pointers, String

---

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

&nbsp;
Example 1:


Input: word1 = &quot;abc&quot;, word2 = &quot;pqr&quot;
Output: &quot;apbqcr&quot;
Explanation:&nbsp;The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


Example 2:


Input: word1 = &quot;ab&quot;, word2 = &quot;pqrs&quot;
Output: &quot;apbqrs&quot;
Explanation:&nbsp;Notice that as word2 is longer, &quot;rs&quot; is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s


Example 3:


Input: word1 = &quot;abcd&quot;, word2 = &quot;pq&quot;
Output: &quot;apbqcd&quot;
Explanation:&nbsp;Notice that as word1 is longer, &quot;cd&quot; is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d


&nbsp;
Constraints:


	1 &lt;= word1.length, word2.length &lt;= 100
	word1 and word2 consist of lowercase English letters.


