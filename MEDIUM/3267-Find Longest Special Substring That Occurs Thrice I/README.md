# Find Longest Special Substring That Occurs Thrice I

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/)

---

# Find Longest Special Substring That Occurs Thrice I

**Difficulty**: Medium

**Tags**: Hash Table, String, Binary Search, Sliding Window, Counting

---

You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string &quot;abc&quot; is not special, whereas the strings &quot;ddd&quot;, &quot;zz&quot;, and &quot;f&quot; are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.

&nbsp;
Example 1:


Input: s = &quot;aaaa&quot;
Output: 2
Explanation: The longest special substring which occurs thrice is &quot;aa&quot;: substrings &quot;aaaa&quot;, &quot;aaaa&quot;, and &quot;aaaa&quot;.
It can be shown that the maximum length achievable is 2.


Example 2:


Input: s = &quot;abcdef&quot;
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.


Example 3:


Input: s = &quot;abcaba&quot;
Output: 1
Explanation: The longest special substring which occurs thrice is &quot;a&quot;: substrings &quot;abcaba&quot;, &quot;abcaba&quot;, and &quot;abcaba&quot;.
It can be shown that the maximum length achievable is 1.


&nbsp;
Constraints:


	3 &lt;= s.length &lt;= 50
	s consists of only lowercase English letters.



