# Split a String in Balanced Strings

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/split-a-string-in-balanced-strings/](https://leetcode.com/problems/split-a-string-in-balanced-strings/)

---

# Split a String in Balanced Strings

**Difficulty**: Easy

**Tags**: String, Greedy, Counting

---

Balanced strings are those that have an equal quantity of &#39;L&#39; and &#39;R&#39; characters.

Given a balanced string s, split it into some number of substrings such that:


	Each substring is balanced.


Return the maximum number of balanced strings you can obtain.

&nbsp;
Example 1:


Input: s = &quot;RLRRLLRLRL&quot;
Output: 4
Explanation: s can be split into &quot;RL&quot;, &quot;RRLL&quot;, &quot;RL&quot;, &quot;RL&quot;, each substring contains same number of &#39;L&#39; and &#39;R&#39;.


Example 2:


Input: s = &quot;RLRRRLLRLL&quot;
Output: 2
Explanation: s can be split into &quot;RL&quot;, &quot;RRRLLRLL&quot;, each substring contains same number of &#39;L&#39; and &#39;R&#39;.
Note that s cannot be split into &quot;RL&quot;, &quot;RR&quot;, &quot;RL&quot;, &quot;LR&quot;, &quot;LL&quot;, because the 2nd and 5th substrings are not balanced.

Example 3:


Input: s = &quot;LLLLRRRR&quot;
Output: 1
Explanation: s can be split into &quot;LLLLRRRR&quot;.


&nbsp;
Constraints:


	2 &lt;= s.length &lt;= 1000
	s[i] is either &#39;L&#39; or &#39;R&#39;.
	s is a balanced string.



