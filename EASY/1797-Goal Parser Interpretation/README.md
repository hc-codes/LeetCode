# Goal Parser Interpretation

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/goal-parser-interpretation/](https://leetcode.com/problems/goal-parser-interpretation/)

---

# Goal Parser Interpretation

**Difficulty**: Easy

**Tags**: String

---

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of &quot;G&quot;, &quot;()&quot; and/or &quot;(al)&quot; in some order. The Goal Parser will interpret &quot;G&quot; as the string &quot;G&quot;, &quot;()&quot; as the string &quot;o&quot;, and &quot;(al)&quot; as the string &quot;al&quot;. The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser&#39;s interpretation of command.

&nbsp;
Example 1:


Input: command = &quot;G()(al)&quot;
Output: &quot;Goal&quot;
Explanation:&nbsp;The Goal Parser interprets the command as follows:
G -&gt; G
() -&gt; o
(al) -&gt; al
The final concatenated result is &quot;Goal&quot;.


Example 2:


Input: command = &quot;G()()()()(al)&quot;
Output: &quot;Gooooal&quot;


Example 3:


Input: command = &quot;(al)G(al)()()G&quot;
Output: &quot;alGalooG&quot;


&nbsp;
Constraints:


	1 &lt;= command.length &lt;= 100
	command consists of &quot;G&quot;, &quot;()&quot;, and/or &quot;(al)&quot; in some order.



